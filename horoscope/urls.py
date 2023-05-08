from django.urls import path
from . import views


urlpatterns = [
    path('<int:sign>', views.sign_number),
    path('<str:sign>', views.sign_name),
]