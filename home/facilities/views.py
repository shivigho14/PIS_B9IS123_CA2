# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def facility_overview(request):
    return render(request, 'facilities/facilities_overview.html')

#templates / facilities


