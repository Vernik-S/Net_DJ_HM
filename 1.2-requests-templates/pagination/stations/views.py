import csv
from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings

stations = []


class Station:
    def __init__(self, name, street, district):
        self.Name = name
        self.Street = street
        self.District = district


def station_init():
    # with open("data-398-2018-08-30.csv", encoding='utf-8') as file:
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        csv_dict = csv.DictReader(file)

        for row in csv_dict:
            stations.append(Station(row["Name"], row["Street"], row["District"]))

        # pprint(stations)


def index(request):
    station_init()

    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = request.GET.get("page", 1)
    paginator = Paginator(stations, 10)
    page = paginator.get_page(page_num)

    context = {
        'bus_stations': page.object_list,
        'page': page
    }
    return render(request, 'stations/index.html', context)
