from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime, os


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time_view'),
        'Показать содержимое рабочей директории': reverse('workdir_view')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().time()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    msg = f'Список файлов в рабочей директории: {os.listdir(os.getcwd())}'
    return HttpResponse(msg)
