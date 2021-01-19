"""URLs for app

author: Yee Hou, Teoh (2471020t)
        # add yr name here if you are working on this file.
"""
from django.contrib import admin
from django.urls import path, include
from cs28 import views

app_name = 'cs28'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cs28', include('django.contrib.auth.urls')),
    path('login/', views.user_login, name='login'),
]
