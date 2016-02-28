from __future__ import unicode_literals

from django.db import models

# Create your models here.


from enum import Enum

from django_enumfield import enum

from django.contrib.auth.models import User

class ColorStyle(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    labels = {
        RED: 'RED COLOR',
        GREEN: 'GREEN COLOR',
        BLUE: 'BLUE COLOR'
    }


class SizeStyle(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

    labels = {
        SMALL: 'SMALL SIZE',
        MEDIUM: 'MEDIUM SIZE',
        LARGE: 'LARGE SIZE'
    }

class Car(models.Model):
    car_owner = models.ForeignKey(User)
    car_name = models.CharField(max_length=100)
    car_color = enum.EnumField(ColorStyle, default=ColorStyle.RED)
    car_size = enum.EnumField(SizeStyle, default=SizeStyle.SMALL)
    car_time_created = models.DateTimeField(auto_now_add=True)
    car_time_changed = models.DateTimeField(auto_now=True)


