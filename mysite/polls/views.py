from django.shortcuts import render,  redirect
# Create your views here.
from django.http import HttpResponse
from .models import Person, Document
from .forms import PersonForm, DocForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.files.storage import FileSystemStorage

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

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print('file name : ', uploaded_file.name)
        print('file size : ', uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'mysite/upload.html', context)

def doc_list(request):
    docs = Document.objects.all()
    return render(request, 'mysite/doc_list.html', {'docs':docs})

def upload_doc(requst):
    if requst.method == 'POST':
        form = DocForm(requst.POST, requst.FILES)
        if form.is_valid():
            form.save()
            return redirect('doc_list')
    else:
        form = DocForm()
    return render(requst, 'mysite/upload_doc.html', {'form':form})