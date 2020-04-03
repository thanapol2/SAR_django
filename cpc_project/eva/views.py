from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .models import Sub_Cate, Main_Cate
from .forms import SubCateFormUpdate,SubCateFormInsert
from django.contrib import messages
from .master_method import Create_Prefix_FromInsert


# method check login
def redircet_login(request):
    if request.user.is_authenticated:
        return 'aa'
    else:
        return redirect('login')

def index(request):
    if request.user.is_authenticated:  # check login
        session_key = request.user.username
        list_main_cate = Main_Cate.objects.filter(username__contains=session_key).order_by('main_topic_id')
        return render(request,'eva/home.html', {'list_main_cate':list_main_cate})
    else:
        return redirect('login')

def page404(request,exception):
    return render(request, 'eva/404.html', status = 404)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def sub_category1_Insert(request):
    if request.user.is_authenticated: #check login
        list_topics = range(1,11)
        if request.method == 'GET':
            context = {}
            for topic in list_topics:
                prefix,form = Create_Prefix_FromInsert('1',topic,request.user.username)
                context[prefix] = form
            return render(request, "eva/sub_category1.html", context)
        else:
            for topic in list_topics:
                prefix = 'form'+str(topic)
                form = SubCateFormInsert(request.POST, prefix=prefix)
                if form.is_valid():
                    form.save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category1_Update(request):
    if request.user.is_authenticated:  # check login
        models = Sub_Cate.objects.filter(sub_no__main_id='1').order_by('sub_no__seq')
        list_topics = range(len(models))  # index list
        context = {}
        if request.method == 'GET':
            for topic in list_topics:
                prefix = 'form' + str(topic+1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormUpdate(prefix=prefix, instance=subcate)
                context[prefix] = form
            return render(request, "eva/sub_category1.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic + 1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormInsert(request.POST, prefix=prefix, instance=subcate)
                context[prefix] = form
                if context[prefix].is_valid():
                    context[prefix].save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category2_Insert(request):
    if request.user.is_authenticated:  # check login
        list_topics = range(1,9)
        if request.method == 'GET':
            context = {}
            for topic in list_topics:
                prefix, form = Create_Prefix_FromInsert('2', topic, request.user.username)
                context[prefix] = form
            return render(request, "eva/sub_category2.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic)
                form = SubCateFormInsert(request.POST, prefix=prefix)
                if form.is_valid():
                    form.save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category2_Update(request):
    if request.user.is_authenticated:  # check login
        models = Sub_Cate.objects.filter(sub_no__main_id='2').order_by('sub_no__seq')
        list_topics = range(len(models))  # index list
        context = {}
        if request.method == 'GET':
            for topic in list_topics:
                prefix = 'form' + str(topic+1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormUpdate(prefix=prefix, instance=subcate)
                context[prefix] = form
            return render(request, "eva/sub_category2.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic + 1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormInsert(request.POST, prefix=prefix, instance=subcate)
                context[prefix] = form
                if context[prefix].is_valid():
                    context[prefix].save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category3_Insert(request):
    if request.user.is_authenticated:  # check login
        list_topics = range(1, 6)
        if request.method == 'GET':
            context = {}
            for topic in list_topics:
                prefix,form = Create_Prefix_FromInsert('3',topic,request.user.username)
                context[prefix] = form
            return render(request, "eva/sub_category3.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic)
                form = SubCateFormInsert(request.POST, prefix=prefix)
                if form.is_valid():
                    form.save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category3_Update(request):
    if request.user.is_authenticated:  # check login
        models = Sub_Cate.objects.filter(sub_no__main_id='3').order_by('sub_no__seq')
        list_topics = range(len(models))  # index list
        context = {}
        if request.method == 'GET':
            for topic in list_topics:
                prefix = 'form' + str(topic+1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormUpdate(prefix=prefix, instance=subcate)
                context[prefix] = form
            return render(request, "eva/sub_category3.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic + 1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormInsert(request.POST, prefix=prefix, instance=subcate)
                context[prefix] = form
                if context[prefix].is_valid():
                    context[prefix].save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category4_Insert(request):
    if request.user.is_authenticated:  # check login
        list_topics = range(1, 4)
        if request.method == 'GET':
            context = {}
            for topic in list_topics:
                prefix,form = Create_Prefix_FromInsert('4',topic,request.user.username)
                context[prefix] = form
            return render(request, "eva/sub_category4.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic)
                form = SubCateFormInsert(request.POST, prefix=prefix)
                if form.is_valid():
                    form.save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category4_Update(request):
    if request.user.is_authenticated:  # check login
        models = Sub_Cate.objects.filter(sub_no__main_id='4').order_by('sub_no__seq')
        list_topics = range(len(models))  # index list
        context = {}
        if request.method == 'GET':
            for topic in list_topics:
                prefix = 'form' + str(topic+1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormUpdate(prefix=prefix, instance=subcate)
                context[prefix] = form
            return render(request, "eva/sub_category4.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic + 1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormInsert(request.POST, prefix=prefix, instance=subcate)
                context[prefix] = form
                if context[prefix].is_valid():
                    context[prefix].save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category5_Insert(request):
    if request.user.is_authenticated:  # check login
        list_topics = range(1,9)
        if request.method == 'GET':
            context = {}
            for topic in list_topics:
                prefix, form = Create_Prefix_FromInsert('5', topic, request.user.username)
                context[prefix] = form
            return render(request, "eva/sub_category5.html", context)
        else:
            for topic in list_topics:
                prefix = 'form'+str(topic)
                form = SubCateFormInsert(request.POST, prefix=prefix)
                if form.is_valid():
                    form.save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')

def sub_category5_Update(request):
    if request.user.is_authenticated:  # check login
        models = Sub_Cate.objects.filter(sub_no__main_id='5').order_by('sub_no__seq')
        list_topics = range(len(models))  # index list
        context = {}
        if request.method == 'GET':
            for topic in list_topics:
                prefix = 'form' + str(topic+1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormUpdate(prefix=prefix, instance=subcate)
                context[prefix] = form
            return render(request, "eva/sub_category5.html", context)
        else:
            for topic in list_topics:
                prefix = 'form' + str(topic + 1)  # plus one for number of topic
                subcate = models[topic]
                form = SubCateFormInsert(request.POST, prefix=prefix, instance=subcate)
                context[prefix] = form
                if context[prefix].is_valid():
                    context[prefix].save()
            messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")
            return redirect('/eva/')
    else:
        return redirect('login')
