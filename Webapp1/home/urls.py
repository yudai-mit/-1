from django.urls import path

from . import views


app_name="home"



urlpatterns = [
    
    path('',views.home,name='home'),
    path('home/edit.html',views.shopinfoview,name='form'),
    
    path('home/sample.html',views.shop,name='shop'),
    
    path('sample2.html',views.shop2,name='shop2'),
    
    path('home/menu.html',views.menu,name='menu'),
    
    path('home/sample2.html',views.shop2,name='shop2'),
    
    path('boxbox.html', views.boxbox,name='boxbox'),
    
    path('<int:id>',views.detail, name='detail'),
    
    
    
    path('index.html',views.home,name='home'),
    
    path('login.html', views.login_view,name='login'),
    
    path('home/login.html', views.login_view,name = 'login'),
    
    path('signup.html', views.signup,name = 'signup'),
    
    
    
   
    
    path('home/index.html',views.home,name='home'),
    
    path('home/index2.html',views.home2,name='home2'),
    
    
    path('home/point.html', views.point,name='point'),
    
    path('home/pointplus.html', views.pointplus,name='pointplus'),
    
    path('home/pointuse.html', views.pointuse,name='pointuse'),
    
    path('confirmed.html',views.confirmed,name ='confirmed'),
    
    path('home/gomibukuro10.html',views.gomibukuro10,name ='gomibukuro10'),
    
    path('home/gomibukuro20.html',views.gomibukuro20,name ='gomibukuro20'),
    
    path('home/gomibukuro30.html',views.gomibukuro30,name ='gomibukuro30'),
    
    path('home/gomibukuro40.html',views.gomibukuro40,name ='gomibukuro40'),
    
    path('home/ticket.html',views.ticket,name ='ticket'),
    
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),




]