from django_filters import rest_framework as filters, DateFromToRangeFilter, ChoiceFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    updated_at = DateFromToRangeFilter()
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        fields = ["updated_at", "status"]
