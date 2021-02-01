"""Django page views.

todo:
- change index to render instead of HttpResponse

author: Yee Hou, Teoh (2471020t)
        Ekaterina Terzieva(2403606t)
        # add yr name here if you are working on this file.
        Kien Welch 2371692w
"""
import csv, io
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def studentUpload(request):
    return render(request,'studentUpload.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('cs28:index'))
    if request.method == "POST":
        # get username and password then check if acc is valid
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('cs28:index'))
            else:
                return HttpResponse("The account you entered is not valid.")

        else:
            # wrong details
            print(f"Invalid login details: {username}, {password}")
            return redirect(reverse('cs28:login'))
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('cs28:index'))


@login_required
def manage(request):
    return render(request, 'manage.html')

@login_required
def module_grades(request):
    return render(request, 'module_grades.html')

@permission_required('admin.can_add_log_entry')
def module_marks_upload(request):
    template = "module_marks_upload.html"
    
    prompt = {
        'order': 'Order of the CSV should be courseCode, matricNo, alphanum'
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        _, created = Grade.objects.update_or_create(
            courseCode=column[0],
            matricNo=column[1],
            alphanum=column[2]
        )
        
        context = {}
        return render(request, template, context)
