from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<em>Hello World!</em>')

# Create your views here.
