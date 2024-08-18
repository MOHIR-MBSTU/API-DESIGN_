# Apidesign/views.py
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse("Welcome to the OnePTE API!")