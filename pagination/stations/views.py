from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    table = list()
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for line in reader:
            line_dict = dict()
            line_dict['Name'] = line['Name']
            line_dict['Street'] = line['Street']
            line_dict['District'] = line['District']
            table.append(line_dict)

    paginator = Paginator(table, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    context = {
         'bus_stations': page.object_list,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
