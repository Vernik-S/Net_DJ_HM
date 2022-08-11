from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, AdvFavUser
from advertisements.permissions import IsOwnerOrAdmin, IsNotDraft
from advertisements.serializers import AdvertisementSerializer, AdvFavSerializer
from django.db.models import Q


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", ]:
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrAdmin()]
        return [(IsNotDraft | IsOwnerOrAdmin)()]  # доп задание DRAFT

    def get_queryset(self):  # доп задание DRAFT
        if self.request.user.is_staff:
            return Advertisement.objects.all()  # админам показываются все объявления
        else:
            qs = Advertisement.objects.filter(
                ~Q(status='DRAFT') | Q(creator=self.request.user.id)
                # юзерам показываются все нечерновики и все объявления юзера
            )
            return qs

    @action(detail=True, methods=["post",], permission_classes=[IsAuthenticated])
    def add_to_fav(self, request, pk):
        #adv = self.get_object()
        user = request.user
        data = {
            "adv": pk,
            "user": user.id,
        }
        serializer = AdvFavSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["delete", ], permission_classes=[IsOwnerOrAdmin])
    def del_from_fav(self, request, pk):
        user = request.user

        AdvFavUser.objects.filter(adv=pk, user=user).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get", ], permission_classes=[IsAuthenticated])
    def get_fav(self, request):
        user = request.user
        qs = AdvFavUser.objects.filter(user=user)
        serializer = AdvFavSerializer(qs, many=True)

        return Response(serializer.data)

