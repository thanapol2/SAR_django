from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Sub_Cate, Main_Cate
from .forms import SubCateForm_Test
from django.http import Http404
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# method check login
def redircet_login(request):
    if request.user.is_authenticated:
        return 'aa'
    else:
        return redirect('login')

def index(request):
    session_key = request.user.username
    list_main_cate = Main_Cate.objects.filter(username__contains=session_key).order_by('main_topic_id')
    return render(request,'eva/home.html', {'list_main_cate':list_main_cate})

def page404(request,exception):
    return render(request, 'eva/404.html', status = 404)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def sub_category1(request, id='0'):
    redircet_login(request)  # add check login
    if request.method == 'GET':
        if id == '0':
            form = SubCateForm_Test()
            form.setValueUsername(request.user.username)
        else:
            subcate1 = Sub_Cate.objects.get(pk=id)
            form = SubCateForm_Test(instance=subcate1)
        return render(request, "eva/sub_category1.html", {'form': form})
    else:
        if id == '0':
            form = SubCateForm_Test(request.POST)
        else:
            subcate1 = Sub_Cate.objects.get(pk=id)
            form = SubCateForm_Test(request.POST, instance=subcate1)
        if form.is_valid():
            form.save()
        return redirect('/eva/')

def sub_category2(request):
    return render(request, 'eva/sub_category2.html')

def sub_category3(request):
    return render(request, 'eva/sub_category3.html')

def sub_category4(request):
    return render(request, 'eva/sub_category4.html')

def sub_category5(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            print('hello')
        else:
            form = SubCateForm_Test()
            return render(request, 'eva/sub_category11.html', {'form': form})
    else:
        return redirect('login')


