from django.db import models
from django.utils import timezone
from PIL import Image
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.shortcuts import render


CHOICES = (
    ("Badnagar", "Badnagar"),
    ("Ghatiya", "Ghatiya"),
    ("Jharda", "Jharda"),
    ("Khachrod", "Khachrod"),
    ("Mahidpur", "Mahidpur"),
    ("Makdone", "Makdone"),
    ("Nagda", "Nagda"),
    ("Tarana", "Tarana"))


class tesil(models.Model):
    Tehsil = models.CharField(max_length=50, choices=CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Fir(models.Model):

    Tehsil = models.CharField(max_length=50, choices=CHOICES)
    Police_station = models.CharField(max_length=50)
    Criminal_address = models.CharField(max_length=50, blank=True,)
    Criminal_name = models.CharField(max_length=100, blank=True,)
    Criminal_mobile_No = models.CharField(max_length=50, blank=True,)
    anonymous = models.BooleanField(default=False)
    Name = models.CharField(max_length=20)
    Permanent_address = models.CharField(max_length=100)
    Mobile_NO = models.CharField(max_length=10)

    place_of_crime = models.CharField(max_length=50)
    Date = models.DateField(default=timezone.localdate())
    Time = models.TimeField(default=timezone.localtime())
    TitleOfCrime = models.CharField(max_length=80)
    content = models.TextField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Feedback_table(models.Model):
    Full_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Message = models.TextField()
