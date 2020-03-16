from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import person

def index(request):
    return render(request, 'mysite/index.html', {'DJANGO_TEST': person.objects.all()})

def login(request):
    return render(request, 'mysite/login.html')