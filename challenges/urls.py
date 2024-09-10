from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("<int:month>", views.monthly_cha_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]