from django.shortcuts import render

def index(request):
    """ A view for the homepage """
    return render(request, 'holidayapp/index.html')
