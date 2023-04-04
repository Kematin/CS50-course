from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("hello")

def flights(request):
    return JsonResponse({"flights": ["f1", "f2", "f3"]})
