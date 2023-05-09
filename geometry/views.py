from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def get_rectangle_area(request, width: int, length: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{length} равна {width * length}')

def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width ** 2}')

def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиуса {radius} равна {3.14 * radius ** 2}')

def redirect_to_figure_rectangle(request, **kwargs):
    redirect_url = reverse('rectangle', args=[*kwargs.values()])
    return HttpResponseRedirect(redirect_url)

def redirect_to_figure_square(request, **kwargs):
    redirect_url = reverse('square', args=[*kwargs.values()])
    return HttpResponseRedirect(redirect_url)

def redirect_to_figure_circle(request, **kwargs):
    redirect_url = reverse('circle', args=[*kwargs.values()])
    return HttpResponseRedirect(redirect_url)
