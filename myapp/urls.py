from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexone,name='homepage'),
    path('aboutus',views.about,name='aboutus'),
    path('dash',views.dashlogin,name='dash'),
    path('doctors',views.doctor,name='doctors'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('bdetails',views.bdetails,name='bdetails'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('appointment',views.appointment,name='appointment'),
    path('comment',views.comment,name='comment'),
    path('contactt',views.contactt,name='contactt'),
    path('registerdata',views.registerdata,name='registerdata'),
    path('logindata',views.logindata,name='logindata'),
    path('logout',views.logout,name='logout'),
    path('ecg',views.ecg,name='ecg'),
    path('pulse',views.pulse,name='pulse'),
    path('temp',views.temp,name='temp'),
]

