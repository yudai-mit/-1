from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render,get_object_or_404
from . import forms
from .forms import SignupForm, LoginForm,SearchForm,Shop
from django.contrib.auth import login,logout
from .models import Pointusing,Shopinfo
from .import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login

def shopinfoview(request):
    form=Shop(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        return render(request,'index2.html')
    else:
        print('ERROR')
    return render(request,'edit.html',{'form':form})
   

def home(request):    
    return render(request,'index.html')
def shop(request):
    """
    articles=Shopinfo.objects.all()
    context={
        'articles':articles
    }
    return render(request,'sample.html',context)"""
    searchForm=SearchForm(request.GET)
    if searchForm.is_valid():
        keyword=searchForm.cleaned_data['keyword']
        articles=Shopinfo.objects.filter(name__contains=keyword)
    
    else:
        searchForm=SearchForm()
        articles=Shopinfo.objects.all()
    
    context={
        'articles': articles,
        'searchForm':searchForm,
    }
    return render(request,'sample.html',context)

def shop2(request):
    """
    articles=Shopinfo.objects.all()
    context={
        'articles':articles
    }
    return render(request,'sample.html',context)"""
    searchForm=SearchForm(request.GET)
    if searchForm.is_valid():
        keyword=searchForm.cleaned_data['keyword']
        articles=Shopinfo.objects.filter(name__contains=keyword)
    
    else:
        searchForm=SearchForm()
        articles=Shopinfo.objects.all()
    
    context={
        'articles': articles,
        'searchForm':searchForm,
    }
    return render(request,'sample2.html',context)

def detail(request,id):
    article=get_object_or_404(Shopinfo,pk=id)
    context={
        'article':article,
    }
    return render(request,'detail.html',context)
     
    
"""    
def upload(request):
    if request.method == "POST":
        form = Shopinfo(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return redirect('home:shop')
    else:
       form = Shopinfo()
    context = {'form':form}
    return render(request, 'edit.html', context)   
 """   

def boxbox(request):    
    return render(request,'boxbox.html')

def menu(request):
    return render(request,'menu.html')
def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request,user)
                return redirect('home/index2.html')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'login.html', param)





def pointuse(request):
    return render(request,'pointuse.html')

def confirmed(request):
    return render(request,"confirmed.html")

def home2(request):
    return render(request,'index2.html')
def edit(request):
    return render(request,'edit.html')

def point(request):
    return render(request,'point.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home/index2.html')
    else:
        form = SignupForm()
    
    param = {
        'form': form
    }
    return render(request,'signup.html',param)


def pointplus(request):
    user = request.user
    user.point = user.point + 100
    user = user.save()
    return render(request,'pointplus.html')

def gomibukuro10(request):
    if request.method == 'POST':
        form = request.POST.get("quantity")
        #print(form)
        user = request.user
        if user.point < int(form)*300:
            param = {"message":"ポイントが足りません"}
            return render(request,'gomibukuro10.html',param)
        data = Pointusing(user=user.username, goods="gomi_10", quantity=form, point=int(form)*300)
        data.save()
        user.point = user.point -( int(form) * 300)
        user = user.save()
        return redirect('point.html')
    
    return render(request,'gomibukuro10.html')

def gomibukuro20(request):
    if request.method == 'POST':
        form = request.POST.get("quantity")
        #print(form)
        user = request.user
        if user.point < int(form)*600:
            param = {"message":"ポイントが足りません"}
            return render(request,'gomibukuro20.html',param)
        data = Pointusing(user=user.username, goods="gomi_20", quantity=form, point=int(form)*600)
        data.save()
        user.point = user.point -( int(form) * 600)
        user = user.save()
        return redirect('point.html')
    
    return render(request,'gomibukuro20.html')

def gomibukuro30(request):
    if request.method == 'POST':
        form = request.POST.get("quantity")
        #print(form)
        user = request.user
        if user.point < int(form)*900:
            param = {"message":"ポイントが足りません"}
            return render(request,'gomibukuro30.html',param)
        data = Pointusing(user=user.username, goods="gomi_30", quantity=form, point=int(form)*900)
        data.save()
        user.point = user.point -( int(form) * 900)
        user = user.save()
        return redirect('point.html')
    
    return render(request,'gomibukuro30.html')

def gomibukuro40(request):
    if request.method == 'POST':
        form = request.POST.get("quantity")
        #print(form)
        user = request.user
        if user.point < int(form)*1200:
            param = {"message":"ポイントが足りません"}
            return render(request,'gomibukuro40.html',param)
        data = Pointusing(user=user.username, goods="gomi_40", quantity=form, point=int(form)*1200)
        data.save()
        user.point = user.point -( int(form) * 1200)
        user = user.save()
        return redirect('point.html')
    
    return render(request,'gomibukuro40.html')

def ticket(request):
    if request.method == 'POST':
        form = request.POST.get("quantity")
        #print(form)
        user = request.user
        if user.point < int(form)*1000:
            param = {"message":"ポイントが足りません"}
            return render(request,'ticket.html',param)
        data = Pointusing(user=user.username, goods="ticket", quantity=form, point=int(form)*1000)
        data.save()
        user.point = user.point -( int(form) * 1000)
        user = user.save()
        return redirect('point.html')
    param={}
    return render(request,'ticket.html')

class TopView(TemplateView):
    template_name = "top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index2.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "login.html"



