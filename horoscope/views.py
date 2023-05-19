from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import render

zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

elements_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

date_dict = {
    1: ['январь', ('capricorn', 1, 20), ('aquarius', 21, 31)],
    2: ['февраль', ('aquarius', 1, 19), ('pisces', 20, 28)],
    3: ['март', ('pisces', 1, 20), ('aries', 21, 31)],
    4: ['апрель', ('aries', 1, 20), ('taurus', 21, 30)],
    5: ['май', ('taurus', 1, 21), ('gemini', 22, 31)],
    6: ['июнь', ('gemini', 1, 21), ('cancer', 22, 30)],
    7: ['июль', ('cancer', 1, 22), ('leo', 23, 31)],
    8: ['август', ('leo', 1, 21), ('virgo', 22, 31)],
    9: ['сентябрь', ('virgo', 1, 23), ('libra', 24, 30)],
    10: ['октябрь', ('libra', 1, 23), ('scorpio', 24, 31)],
    11: ['ноябрь', ('scorpio', 1, 22), ('sagittarius', 23, 30)],
    12: ['декабрь', ('sagittarius', 1, 22), ('capricorn', 23, 31)],
}

def elements(request):
    temp_res = ''
    for el in list(elements_dict):
        redirect_path = reverse('horoscope-elements', args=[el])
        temp_res += f"<li> <a href={redirect_path}>{el.title()} </a> </li>"
    response = f"""<ul>{temp_res}</ul>"""
    return HttpResponse(response)


def element(request, element: str):
    if element in elements_dict:
        response = ''
        for sign_z in elements_dict[element]:
            redirect_path = reverse('horoscope-name', args=[sign_z])
            response += f"<li> <a href={redirect_path}>{sign_z} </a> </li>"
        return HttpResponse(f'<ol>{response}</ol>')


def sign_number(request, sign: int):
    if sign > len(list(zodiac_dict)):
        return HttpResponseNotFound(f'Нет такого знака задиака {sign}')
    zodiacs = list(zodiac_dict)[sign - 1]
    redirect_url = reverse('horoscope-name', args=[zodiacs])
    return HttpResponseRedirect(redirect_url)


def sign_name(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    sign_name = description.split()[0]
    context = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiacs,
        'sign_name': sign_name
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_info_by_date(request, month, day):
    if month in date_dict:
        name_month, sign1, sign2, = date_dict[month]
        match sign2:
            case name_sign, start_day, end_day if start_day <= day <= end_day:
                redirect_url = reverse('horoscope-name', args=[name_sign])
                return HttpResponseRedirect(redirect_url)
        match sign1:
            case name_sign, start_day, end_day if start_day <= day <= end_day:
                redirect_url = reverse('horoscope-name', args=[name_sign])
                return HttpResponseRedirect(redirect_url)
            case _:
                return HttpResponse(f'Нет такого дня {day} в месяце {name_month}')
    return HttpResponse(f'Нет такого месяца {month}')

def index_info(request):
    sign_zodiac = list(zodiac_dict)
    context = {
        'zodiacs': sign_zodiac
    }
    return render(request, 'horoscope/index.html', context=context)




