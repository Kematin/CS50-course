from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Airport, Flight, Passenger

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
    # find all passengers, who not in flight
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    context = {
            "flight": flight,
            "passengers": passengers,
            "non_passengers": non_passengers,
        }
    return render(request, "flight.html", context)


def book(request, flight_id):
    # if a post request, add new passenger
    if request.method == "POST":
        
        # accesing flight
        flight = Flight.objects.all().get(id=flight_id)

        # find id passenger from submitted data
        passenger_id = int(request.POST["passengers"])

        # find passenger from based id
        passenger = Passenger.objects.get(pk=passenger_id)

        # add new passenger in flight
        passenger.flights.add(flight)

        # redirect user to flight route
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
