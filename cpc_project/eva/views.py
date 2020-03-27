from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Sub_Cate11
from .forms import SubCateForm11

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
    print(request.method)
    if request.method == 'POST':
        data = request.POST["no11"]
        print(data)
    else:
        return render(request, 'eva/sub_category1.html')

def sub_category2(request):
    return render(request, 'eva/sub_category2.html')

def sub_category3(request):
    return render(request, 'eva/sub_category3.html')

def sub_category4(request):
    return render(request, 'eva/sub_category4.html')

def sub_category5(request):
    return render(request, 'eva/sub_category5.html')

# def add_form_no11(request):
#     no11 = request.POST["no11"]
#     txtUsername11 = request.POST["txtUsername11"]
#     txtWeight11 = request.POST["txtWeight11"]
#     txtTarget11 = request.POST["txtTarget11"]
#
#     form_no11_info = Sub_Cate11(no11=no11,txtUsername11=txtUsername11,txtWeight11=txtWeight11,txtTarget11=txtTarget11)
#     form_no11_info.save()
#     return render(request, "eva/sub_category1.html")

