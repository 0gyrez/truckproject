from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.get_trucks, name='main'),
    path('', views.main_page, name='main_page'),
    path('main/<int:truck_id>/', views.get_truck, name='truck'),
    path('register/', views.register, name='register'),
    path('login/', views.login_v, name='login_v'),


]