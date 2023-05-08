from django.urls import path, reverse
from . import views


urlpatterns = [
    path('<int:day>', views.days_number),
    path('<str:day>', views.days_name, name='d-w'),
]