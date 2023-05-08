from django.urls import path
from . import views


urlpatterns = [
    path('<int:day>', views.days_number),
    path('<str:day>', views.days_name),
]