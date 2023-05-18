from django.urls import path, register_converter
from . import views


urlpatterns = [
    path('', views.index_info, name='horoscope-index'),
    path('type', views.elements),
    path('type/<str:element>', views.element, name='horoscope-elements'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:sign>', views.sign_number),
    path('<str:sign>', views.sign_name, name='horoscope-name'),
]