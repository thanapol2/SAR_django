from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404

def index(request):
    return render(request,'eva/home.html')

def page404(request,exception):
    return render(request, 'eva/404.html', status = 404)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def sub_category1(request):
    return render(request, 'eva/sub_category1.html')

def sub_category2(request):
    return render(request, 'eva/sub_category2.html')

def sub_category3(request):
    return render(request, 'eva/sub_category3.html')

def sub_category4(request):
    return render(request, 'eva/sub_category4.html')

def sub_category5(request):
    return render(request, 'eva/sub_category5.html')
