# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-07 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.TextField()),
                ('custID', models.TextField()),
                ('RoomNo', models.TextField()),
                ('CheckinDate', models.DateTimeField(auto_now_add=True)),
                ('CheckOutDate', models.DateTimeField(auto_now_add=True)),
                ('TotalCost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='NewCustomerReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.TextField()),
                ('title', models.TextField()),
                ('Address', models.TextField()),
                ('IDType', models.TextField()),
                ('IDNumber', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RegisterNewEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpName', models.TextField()),
                ('IDType', models.TextField()),
                ('IDNumber', models.TextField()),
                ('Address', models.TextField()),
                ('BloodGroup', models.TextField()),
                ('DOB', models.DateTimeField(auto_now_add=True)),
                ('Wage', models.FloatField()),
                ('Desc', models.TextField()),
                ('Designation', models.TextField()),
                ('SocialSecNo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RegisterNewFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacilityName', models.TextField()),
                ('BuildingNo', models.IntegerField()),
                ('Floor', models.IntegerField()),
                ('Description', models.TextField()),
                ('MinorsAllowed', models.TextField()),
            ],
        ),
    ]
