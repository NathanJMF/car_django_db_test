from django.shortcuts import render
from django.template import RequestContext, Template
from django.template.loader import get_template
from django.template.response import TemplateResponse

from garage.models import get_limited_car_set


def garage_home(request):
    car_set = get_limited_car_set()
    return TemplateResponse(request, "car_home.html", {"car_set": car_set})
