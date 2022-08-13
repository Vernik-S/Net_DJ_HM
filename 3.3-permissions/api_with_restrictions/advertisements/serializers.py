from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, AdvFavUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        # валидация для всех POST и для PUT и PUTCH если статус OPEN
        if self.context["request"].method == "POST" or \
                (self.context["request"].method in ["PUT", "PATCH"] and
                 self.context["request"].data.get("status") == "OPEN"):
            qs = Advertisement.objects.filter(creator=self.context["request"].user, status="OPEN")
            #print(qs.count())
            if qs.count() >= 10: raise ValidationError("Не больше десяти открытых объявлений для пользователя")

        return data


class AdvFavSerializer(serializers.ModelSerializer):
   # user = UserSerializer(
   #     read_only=True,
   # )

    class Meta:
        model = AdvFavUser
        fields = ('id', 'adv', 'user')

    # def create(self, validated_data):
    #     validated_data["user"] = self.context["request"].user
    #     return super().create(validated_data)

    def validate(self, data):

        #if self.context["request"].method == "POST":
        if data["adv"].creator == data["user"]:
            raise ValidationError("Нельзя добавлять в избранное собственные сообщения")

        return data
