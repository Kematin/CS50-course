from django.shortcuts import render
from .models import Airport, Flight

# Create your views here.

def index(request):
    context = {
            "airports": Airport.objects.all(),
            "flights": Flight.objects.all(),
        }
    return render(request, "index.html", context)

def flight(request, flight_id):
    flight = Flight.objects.all().get(id=flight_id)
    passengers = flight.passengers.all()
    context = {
            "flight": flight,
            "passengers": passengers,
        }
    return render(request, "flight.html", context)
