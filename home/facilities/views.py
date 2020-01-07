# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def facility_overview(request):
    return render(request, 'facilities/facilities_overview.html')

#templates / facilities


from .models import Product
from .forms import ProductForm

def product_detail_view(request):
    obj=Product.objects.get(id=1)
    context={
        'title':obj.title,
        'desc':obj.desc
    }
    # context={'object':obj}
    # then use obj.ttitle and obj.desc in the templates file


    return render(request,"detail.html",context)



def product_crea_view(request):
    # form =ProductForm(request.POST or None)
    form =ProductForm(request.POST)
    if form.is_valid():
        form.save()
        form=ProductForm()
    else:
            print form.errors
    context={'form':form}
    return render(request,"create.html",context)