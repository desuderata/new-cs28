"""Django page views.

todo:
- change index to render instead of HttpResponse

author: Yee Hou, Teoh (2471020t)
        # add yr name here if you are working on this file.
"""
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')
