"""Population script

author: Yee Hou, Teoh (2471020t)
"""

import os
import django
import random
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs28_project.settings')
django.setup()

from django.contrib.auth.models import User
from cs28.models import GraduationYear, AcademicPlan


def populate_users():
    # Admin user
    admin, _ = User.objects.get_or_create(username="admin",
                                          email="admin@a.a")
    admin.is_staff = True
    admin.is_superuser = True
    admin.save()

    admin.set_password("password")
    admin.save()
    print("Created superuser...")

    # Staff user
    staff, _ = User.objects.get_or_create(username="staff",
                                          email="staff@a.a")
    staff.is_staff = True
    staff.save()

    staff.set_password("password")
    staff.save()
    print("Created staff user...")

    # Normal user
    user, _ = User.objects.get_or_create(username="user",
                                         email="user@a.a")
    user.save()

    user.set_password("password")
    user.save()
    print("Created normal user...")


def populate_graduation_year():
    GraduationYear.objects.get_or_create(gradYear="15-16")
    GraduationYear.objects.get_or_create(gradYear="16-17")
    GraduationYear.objects.get_or_create(gradYear="17-18")
    GraduationYear.objects.get_or_create(gradYear="18-19")
    GraduationYear.objects.get_or_create(gradYear="19-20")
    GraduationYear.objects.get_or_create(gradYear="20-21")
    print("Populated graduation year...")


def populate_academic_plan():
    year_19_20 = GraduationYear.objects.get(gradYear="19-20")
    AcademicPlan.objects.get_or_create(gradYear=year_19_20,
                                       planCode="F100-2208",
                                       courseCode="CHEM-4H",
                                       mcName="Chemistry, BSc",
                                       course_1="CHEM_3012", weight_1=0.083,
                                       course_2="CHEM_3009", weight_2=0.083,
                                       course_3="CHEM_3014", weight_3=0.083,
                                       course_4="CHEM_4003P", weight_4=0.25,
                                       course_5="CHEM_4014", weight_5=0.125,
                                       course_6="CHEM_4012", weight_6=0.125,
                                       course_7="CHEM_4009", weight_7=0.125,
                                       course_8="CHEM_4001", weight_8=0.125,
                                       )
    year_20_21 = GraduationYear.objects.get(gradYear="20-21")
    AcademicPlan.objects.get_or_create(gradYear=year_20_21,
                                       planCode="F101-2207",
                                       courseCode="CHEM-5M",
                                       mcName="Chemistry with WP,MSci",
                                       course_1="CHEM_4012", weight_1=0.057,  # Org 3
                                       course_2="CHEM_4009", weight_2=0.057,  # Inorg 3
                                       course_3="CHEM_4014", weight_3=0.057,  # Phys 3
                                       course_4="CHEM_5016", weight_4=0.029,  # Front 3
                                       course_5="CHEM_4025", weight_5=0.200,  # Placement
                                       course_6="CHEM_5009P", weight_6=0.171,  # Project
                                       course_7="CHEM_5022", weight_7=0.086,  # Phys 4
                                       course_8="CHEM_5021", weight_8=0.086,  # Org 4
                                       course_9="CHEM_5017", weight_9=0.086,  # Inorg 4
                                       course_10="CHEM_5003", weight_10=0.086,  # ST
                                       course_11="CHEM_5005", weight_11=0.086,  # Prob
                                       )
    print("Populate Academic plans...")


def populate():
    populate_users()
    populate_graduation_year()
    populate_academic_plan()

if __name__ == '__main__':
    print("Populating cs28 database")
    populate()
