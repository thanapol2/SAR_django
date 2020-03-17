from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import Person

def index(request):
    all_person = Person.objects.all()
    return render(request, 'mysite/index.html', {'all_person': all_person})

def detail(request, p_id):
    try:
        person = Person.objects.get(pk=p_id)
    except Person.DoesNotExist:
        raise Http404("Person does not exist")
    return render(request, 'mysite/detail.html', {'person': person})

def login(request):
    return render(request, 'mysite/login.html')
