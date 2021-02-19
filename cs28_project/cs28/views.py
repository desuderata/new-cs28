"""Django page views.

author: Yee Hou, Teoh (2471020t)
        Ekaterina Terzieva(2403606t)
        # add yr name here if you are working on this file.
        Kien Welch 2371692w
        Alana Grant 239048G
"""
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from decimal import localcontext, Decimal, ROUND_HALF_UP
import numpy as np

from cs28.models import Student
from cs28.models import Grade


def index(request):
    return render(request, 'index.html')


def studentUpload(request):
    return render(request, 'studentUpload.html')


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
    ctx = {"student": Student.objects.all()}
    return render(request, 'manage.html', context=ctx)


@login_required
def module_grades(request):
    ctx = {"grade": Grade.objects.all()}
    return render(request, 'module_grades.html', context=ctx)


@login_required
def calculate(request):
    if request.method != "POST":
        if len(request.data) > 0:
            students = Student.object.filter(gradeDataUpdated=True,
                                             gradYear__in=request.data)
        else:
            students = Student.objects.filter(gradeDataUpdated=True)

        course_counts = {}
        course_weights = {}

        for student in students.iterator():
            academic_plan = student.academicPlan
            plan_code = academic_plan.planCode
            weights = academic_plan.get_weights()
            courses = academic_plan.get_courses()

            numerical_score = []
            weight_list = []

            # get number of courses
            if plan_code not in course_counts.keys():
                # remove none values to get num of courses
                course_counts[plan_code] = len([c for c in courses if c])

            course_count = course_counts[plan_code]
            # get weight for academic plan
            if plan_code not in course_weights.keys():
                course_weights[plan_code] = {
                    courses[i]: weights[i] for i in range(course_count)}

            grades = Grade.objects.filter(matricNo=student.matricNo)
            # check if a course is missing
            is_missing_grades = course_count != len(grades)
            has_special_code = False

            for grade in grades.iterator():
                if grade.is_grade_a_special_code():
                    has_special_code = True
                    continue

                if grade.courseCode not in courses:
                    is_missing_grades = True
                    continue

                # dot of vec to get sum of all weighted scores
                numerical_score.append(grade.get_alphanum_as_num())
                weight_list.append(course_weights[plan_code][grade.courseCode])
                overall_points = np.dot(weight_list, numerical_score)

            # Rounding: quantize for half up rounding
            def round(flt, dec):
                return Decimal(str(flt)).quantize(Decimal(dec),
                                                  rounding=ROUND_HALF_UP)

            student.finalAward1 = round(overall_points, "0.0")
            student.finalAward2 = round(overall_points, "0.0")
            student.finalAward3 = round(overall_points, "0.0")
            student.finalAward4 = round(overall_points, "0.0")

            student.set_is_missing_grades(is_missing_grades)
            student.set_has_special_code(has_special_code)

        students.update(gradeDataUpdated=False)
        return HttpResponse(status=201)
    return HttpResponse(status=400)
