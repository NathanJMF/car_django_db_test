from django.urls import path
from . import views

urlpatterns = [
    path("", views.garage_home)
]
