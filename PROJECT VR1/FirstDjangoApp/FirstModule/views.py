from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def FirstModule(request):
    return HttpResponse("Welcome to Ayushi Project")
    