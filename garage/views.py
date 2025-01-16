from django.shortcuts import render
from django.template import RequestContext, Template
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from garage.forms import CarForm
from garage.models import Car, Owner, CarBrand
from garage.models import get_limited_car_set


class GarageList(ListView):
    queryset = get_limited_car_set()


class GarageDetailView(DetailView):
    model = Car


class GarageCarCreateView(FormView):
    form_class = CarForm
    template_name = "garage/car_form.html"
    success_url = reverse_lazy("view_all_car")

    def form_valid(self, form):
        owner_object, owner_created_flag = Owner.objects.get_or_create(
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"]
        )
        brand_object, brand_created_flag = CarBrand.objects.get_or_create(
            name=form.cleaned_data["name"],
            num_seats = form.cleaned_data["num_seats"],
            num_wheel = form.cleaned_data["num_wheel"],
            very_very_large_data_field = {}
        )
        car = Car.objects.create(brand=brand_object, owner=owner_object)
        return super().form_valid(form)
