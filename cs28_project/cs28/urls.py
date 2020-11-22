"""URLs for app

author: Yee Hou, Teoh (2471020t)
        # add yr name here if you are working on this file.
"""
from django.urls import path
from cs28 import views

app_name = 'cs28'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]
