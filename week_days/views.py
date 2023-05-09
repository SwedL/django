from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

days_week = {'monday': 'Купить хлеб',
             'tuesday': 'Помыть машину',
             'wednesday': 'Покормить кота',
             'thursday': 'Выучить уроки',
             'friday': 'Постирать бельё',
             'saturday': 'Посмотреть кино',
             'sunday': 'Выспаться'}

def days_name(request, day):
    if day in list(days_week):
        return HttpResponse(f'Нужно {days_week[day]}')
    return HttpResponse(f'Нет такого дня недели {day}')

def days_number(request, day):
    if day > len(list(days_week)):
        return HttpResponseNotFound(f'Нет такого дня недели {day}')
    need_day = list(days_week)[day-1]
    redirect_url = reverse('dw-name', args=[need_day])
    return HttpResponseRedirect(redirect_url)

