from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Sub_Cate, Main_Cate
from .forms import SubCateFormUpdate,SubCateFormInsert
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

def sub_category1_Insert(request):
    if request.user.is_authenticated: #check login
        if request.method == 'GET':
            form1 = SubCateFormInsert(prefix="form1")
            form1.setValueSubNo('11')
            form1.setValueUsername(request.user.username)
            form2 = SubCateFormInsert(prefix="form2")
            form2.setValueSubNo('12')
            form2.setValueUsername(request.user.username)
            form3 = SubCateFormInsert(prefix="form3")
            form3.setValueSubNo('13')
            form3.setValueUsername(request.user.username)
            form4 = SubCateFormInsert(prefix="form4")
            form4.setValueSubNo('14')
            form4.setValueUsername(request.user.username)
            form5 = SubCateFormInsert(prefix="form5")
            form5.setValueSubNo('15')
            form5.setValueUsername(request.user.username)
            form6 = SubCateFormInsert(prefix="form6")
            form6.setValueSubNo('16')
            form6.setValueUsername(request.user.username)
            form7 = SubCateFormInsert(prefix="form7")
            form7.setValueSubNo('17')
            form7.setValueUsername(request.user.username)
            form8 = SubCateFormInsert(prefix="form8")
            form8.setValueSubNo('18')
            form8.setValueUsername(request.user.username)
            form9 = SubCateFormInsert(prefix="form9")
            form9.setValueSubNo('19')
            form9.setValueUsername(request.user.username)
            form10 = SubCateFormInsert(prefix="form10")
            form10.setValueSubNo('110')
            form10.setValueUsername(request.user.username)
            context = {
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5,
                'form6': form6, 'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10,
            }
            return render(request, "eva/sub_category1.html", context)
        else:
            form1 = SubCateFormInsert(request.POST)
            form2 = SubCateFormInsert(request.POST)
            form3 = SubCateFormInsert(request.POST)
            form4 = SubCateFormInsert(request.POST)
            form5 = SubCateFormInsert(request.POST)
            form6 = SubCateFormInsert(request.POST)
            form7 = SubCateFormInsert(request.POST)
            form8 = SubCateFormInsert(request.POST)
            form9 = SubCateFormInsert(request.POST)
            form10 = SubCateFormInsert(request.POST)

            if form1.is_valid():
                form1.save()
            elif form2.is_valid():
                form2.save()
            elif form3.is_valid():
                form3.save()
            elif form4.is_valid():
                form4.save()
            elif form5.is_valid():
                form5.save()
            elif form6.is_valid():
                form6.save()
            elif form7.is_valid():
                form7.save()
            elif form8.is_valid():
                form8.save()
            elif form9.is_valid():
                form9.save()
            elif form10.is_valid():
                form10.save()
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category1_Update(request):
    if request.user.is_authenticated:  # check login
        if request.method == 'GET':
            id = '4'
            subcate1 = Sub_Cate.objects.get(pk=id)
            form = SubCateFormUpdate(instance=subcate1)
            return render(request, "eva/sub_category1.html", {'form': form})
        else:
            id = '4'
            subcate1 = Sub_Cate.objects.get(pk=id)
            form = SubCateFormInsert(request.POST, instance=subcate1)
            if form.is_valid():
                form.save()
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category2(request):
    if request.user.is_authenticated:  # check login
        if request.method == 'GET':
            form1 = SubCateFormInsert(prefix="form1")
            form1.setValueSubNo('21')
            form1.setValueUsername(request.user.username)
            form2 = SubCateFormInsert(prefix="form2")
            form2.setValueSubNo('22')
            form2.setValueUsername(request.user.username)
            form3 = SubCateFormInsert(prefix="form3")
            form3.setValueSubNo('23')
            form3.setValueUsername(request.user.username)
            form4 = SubCateFormInsert(prefix="form4")
            form4.setValueSubNo('24')
            form4.setValueUsername(request.user.username)
            form5 = SubCateFormInsert(prefix="form5")
            form5.setValueSubNo('25')
            form5.setValueUsername(request.user.username)
            form6 = SubCateFormInsert(prefix="form6")
            form6.setValueSubNo('26')
            form6.setValueUsername(request.user.username)
            form7 = SubCateFormInsert(prefix="form7")
            form7.setValueSubNo('27')
            form7.setValueUsername(request.user.username)
            form8 = SubCateFormInsert(prefix="form8")
            form8.setValueSubNo('28')
            form8.setValueUsername(request.user.username)

            context = {
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5,
                'form6': form6, 'form7': form7, 'form8': form8,
            }
            return render(request, "eva/sub_category2.html", context)
        else:
            form1 = SubCateFormInsert(request.POST)
            form2 = SubCateFormInsert(request.POST)
            form3 = SubCateFormInsert(request.POST)
            form4 = SubCateFormInsert(request.POST)
            form5 = SubCateFormInsert(request.POST)
            form6 = SubCateFormInsert(request.POST)
            form7 = SubCateFormInsert(request.POST)
            form8 = SubCateFormInsert(request.POST)

            if form1.is_valid():
                form1.save()
            elif form2.is_valid():
                form2.save()
            elif form3.is_valid():
                form3.save()
            elif form4.is_valid():
                form4.save()
            elif form5.is_valid():
                form5.save()
            elif form6.is_valid():
                form6.save()
            elif form7.is_valid():
                form7.save()
            elif form8.is_valid():
                form8.save()
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category3(request):
    if request.user.is_authenticated:  # check login
        if request.method == 'GET':
            form1 = SubCateFormInsert(prefix="form1")
            form1.setValueSubNo('31')
            form1.setValueUsername(request.user.username)
            form2 = SubCateFormInsert(prefix="form2")
            form2.setValueSubNo('32')
            form2.setValueUsername(request.user.username)
            form3 = SubCateFormInsert(prefix="form3")
            form3.setValueSubNo('33')
            form3.setValueUsername(request.user.username)
            form4 = SubCateFormInsert(prefix="form4")
            form4.setValueSubNo('34')
            form4.setValueUsername(request.user.username)
            form5 = SubCateFormInsert(prefix="form5")
            form5.setValueSubNo('35')
            form5.setValueUsername(request.user.username)

            context = {
                'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5,
            }
            return render(request, "eva/sub_category3.html", context)
        else:
            form1 = SubCateFormInsert(request.POST)
            form2 = SubCateFormInsert(request.POST)
            form3 = SubCateFormInsert(request.POST)
            form4 = SubCateFormInsert(request.POST)
            form5 = SubCateFormInsert(request.POST)

            if form1.is_valid():
                form1.save()
            elif form2.is_valid():
                form2.save()
            elif form3.is_valid():
                form3.save()
            elif form4.is_valid():
                form4.save()
            elif form5.is_valid():
                form5.save()
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category4(request):
    if request.user.is_authenticated:  # check login
        if request.method == 'GET':
            form1 = SubCateFormInsert(prefix="form1")
            form1.setValueSubNo('41')
            form1.setValueUsername(request.user.username)
            form2 = SubCateFormInsert(prefix="form2")
            form2.setValueSubNo('42')
            form2.setValueUsername(request.user.username)
            form3 = SubCateFormInsert(prefix="form3")
            form3.setValueSubNo('43')
            form3.setValueUsername(request.user.username)
            context = {
                'form1': form1, 'form2': form2, 'form3': form3,
            }
            return render(request, "eva/sub_category4.html", context)
        else:
            form1 = SubCateFormInsert(request.POST)
            form2 = SubCateFormInsert(request.POST)
            form3 = SubCateFormInsert(request.POST)

            if form1.is_valid():
                form1.save()
            elif form2.is_valid():
                form2.save()
            elif form3.is_valid():
                form3.save()
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category5(request):
    if request.user.is_authenticated:  # check login
        list_topics = range(1,9)
        if request.method == 'GET':
            context = {}
            for topic in list_topics:
                prefix = 'form'+str(topic)
                SubNo = str('5')+str(topic)
                form = SubCateFormInsert(prefix=prefix)
                form.setValueSubNo(SubNo)
                form.setValueUsername(request.user.username)
                context[prefix] = form
            return render(request, "eva/sub_category5.html", context)
        else:
            for topic in list_topics:
                prefix = 'form'+str(topic)
                form = SubCateFormInsert(request.POST, prefix=prefix)
                if form.is_valid():
                    form.save()
            return redirect('/eva/')
    else:
        return redirect('login')


