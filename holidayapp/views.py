from django.shortcuts import render
from .models import Apartment
# from django.views import generic


def index(request):
    """ A view to return the homepage """
    apartments = Apartment.objects.all()
    template = 'holidayapp/index.html'
    context = {
        'apartments': apartments,
    }

    return render(request, template, context)

def apartments_view(request):
    """ A page to view apartments """
    apartments = Apartment.objects.all()
    template = 'holidayapp/apartments.html'
    context = {
        'apartments': apartments,
    }

    return render(request, template, context)
