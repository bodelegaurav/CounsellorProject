from django.contrib import admin
from django.urls import path, include
from frus import views

urlpatterns = [
    path('',views.home,name="home"),
    path('index',views.index,name="index"),
    path('Book/',views.book,name="book"),
    path('counsellor/',views.coun,name="counsellor"),
    path('RakeshKakati/',views.rk,name="RakeshKakati"),
    path('NamrataR/',views.f1,name="NamrataR"),
    path('Book/handleA',views.Happo,name="handleA"),
    path('PallabitaC/',views.f2,name="PallabitaC"),
    path('login',views.handleLogin,name="handleLogin"),
    path('logout',views.handleLogout,name="handleLogout"),
    path('signup',views.handleSignup,name="handleSignup"),
    path('contact',views.contact,name="contact"),
    path('',views.index, name='index'),
    path('ibs',views.ibs, name='ibs'),
    path('chat/<str:room_name>/', views.room, name='room'),
]