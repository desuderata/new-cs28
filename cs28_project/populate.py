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
from cs28.models import GraduationYear


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


def populate():
    populate_users()


if __name__ == '__main__':
    print("Populating cs28 database")
    populate()
