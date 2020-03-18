from django.shortcuts import render,  redirect
# Create your views here.
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm

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
        return redirect('/person/list/')

def person_delete(request, id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('/person/list/')




# def index(request):
#     all_person = Person.objects.all()
#     return render(request, 'mysite/index.html', {'all_person': all_person})

# def detail(request, p_id):
#     try:
#         person = Person.objects.get(pk=p_id)
#     except Person.DoesNotExist:
#         raise Http404("Person does not exist")
#     return render(request, 'mysite/detail.html', {'person': person})

# def login(request):
#     return render(request, 'mysite/login.html')
