from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Sub_Cate1, Main_Cate
from .forms import SubCateForm11
from .forms import SubCateForm22
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

def sub_category1(request):
    redircet_login(request)  # add check login
    if request.method == 'POST':
        no11 = request.POST["no11"]
        txtUsername11 = request.POST["txtUsername11"]
        txtWeight11 = request.POST["txtWeight11"]
        txtTarget11 = request.POST["txtTarget11"]
        print(no11,txtUsername11,txtWeight11,txtTarget11)
        form_no11_info = Sub_Cate1(sub_no=no11, username=txtUsername11, weight=txtWeight11, target=txtTarget11)
        form_no11_info.save()
        return render(request, 'eva/sub_category1.html')
    else:
        session_key = request.user.username
        return render(request, 'eva/sub_category1.html')

def update_sub_category1(request):
    edit_sub_cate11 = Sub_Cate1.objects.filter(sub_no__istartswith='1')
    print(edit_sub_cate11)
    return render(request, 'eva/sub_category1.html', {'edit_sub_cate11':edit_sub_cate11})

# def update_sub_category2(request):
#     edit_sub_cate22 = Sub_Cate11.objects.filter(sub_no__contains='22')
#     print(edit_sub_cate22)
#     return render(request, 'eva/sub_category2.html', {'edit_sub_cate22':edit_sub_cate22})

def sub_category2(request):
    return render(request, 'eva/sub_category2.html')

def sub_category3(request):
    return render(request, 'eva/sub_category3.html')

def sub_category4(request):
    return render(request, 'eva/sub_category4.html')

def sub_category5(request):
    if request.method == 'POST':
        print('hello')
    else:
        form = SubCateForm22()
        return render(request, 'eva/sub_category11.html', {'form': form})

# def add_form_no11(request):
#     no11 = request.POST["no11"]
#     txtUsername11 = request.POST["txtUsername11"]
#     txtWeight11 = request.POST["txtWeight11"]
#     txtTarget11 = request.POST["txtTarget11"]
#
#     form_no11_info = Sub_Cate11(no11=no11,txtUsername11=txtUsername11,txtWeight11=txtWeight11,txtTarget11=txtTarget11)
#     form_no11_info.save()
#     return render(request, "eva/sub_category1.html")

