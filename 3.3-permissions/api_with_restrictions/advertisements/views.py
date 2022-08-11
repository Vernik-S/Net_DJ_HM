from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrAdmin, IsNotDraft
from advertisements.serializers import AdvertisementSerializer
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
            return Advertisement.objects.all() #админам показываются все объявления
        else:
            qs = Advertisement.objects.filter(
                ~Q(status='DRAFT') | Q(creator=self.request.user.id) #юзерам показываются все нечерновики и все объявления юзера
            )
            return qs
