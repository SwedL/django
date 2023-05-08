from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

sign_zodiac = {
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

def sign_number(request, sign: int):
    if sign > len(list(sign_zodiac)):
        return HttpResponseNotFound(f'Нет такого знака задиака {sign}')
    zodiacs = list(sign_zodiac)[sign-1]
    return HttpResponseRedirect(zodiacs)

def sign_name(request, sign: str):
    if sign in list(sign_zodiac):
        return HttpResponse(f'знак зодиака {sign_zodiac[sign]}')
    return HttpResponseNotFound(f'Нет такого знака задиака {sign}')
