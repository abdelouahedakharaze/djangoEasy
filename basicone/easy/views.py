from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def wellcome(request):
    return HttpResponse("Welcome to the Basic One app!")