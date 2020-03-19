from django.shortcuts import render,  redirect
# Create your views here.
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def person_list(request):
    context = {'person_list':Person.objects.all()}
    return render(request, "mysite/list.html", context)

def person_form(request, id='0'):
    if request.method == "GET":
        if id == '0':
            form = PersonForm()
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(instance=person)
        return render(request, "mysite/form.html", {'form':form})
    else:
        if id == '0':
            form = PersonForm(request.POST)
        else:
            person = Person.objects.get(pk=id)
            form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return redirect('/list/')

def person_delete(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('/list/')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/list/')
    else:
        form = AuthenticationForm()

    return render(request, 'mysite/login.html', {'form':form})
