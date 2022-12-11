from django.shortcuts import render
from .models import Airport, Flight

# Create your views here.

def index(request):
    context = {
            "airports": Airport.objects.all(),
            "flights": Flight.objects.all(),
        }
    return render(request, "index.html", context)
