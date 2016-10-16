
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def hello_poll(request):
    return HttpResponse("Polls View!")

def second_poll(request):
    return HttpResponse("second Polls View!")