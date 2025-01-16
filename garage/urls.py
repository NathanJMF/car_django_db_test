from django.urls import path
from . import views
from .views import GarageList, GarageDetailView, GarageCarCreateView

urlpatterns = [
    path("", GarageList.as_view(), name="view_all_car"),
    path("<int:pk>/", GarageDetailView.as_view(), name="view_single_car"),
    path("create_car/", GarageCarCreateView.as_view(), name="create_car")
]
