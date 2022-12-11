from django.shortcuts import render
from .models import Flight

# Create your views here.

def index(request):
    context = {
            "flights": Flight.objects.all()
        }
    return render(request, "index.html", context)
