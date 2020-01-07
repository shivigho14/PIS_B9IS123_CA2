# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class RoomsInHotel(models.Model):
    RoomNumber= models.CharField(max_length=100)
    RoomFacility=models.CharField(max_length=100)
    RoomLocationFloor=models.CharField(max_length=100)
    dateAdded=models.DateTimeField(auto_now_add=True) #automatically gets current time when the room is created
    Notes=models.CharField(max_length=100)
    #add any other fields required here

    def __str__(self):
        return self.RoomNumber


class Product(models.Model):
    title=models.TextField()
    desc=models.TextField()
    price=models.TextField()
    summary=models.TextField(default='default text')
    