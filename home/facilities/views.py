# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def facility_overview(request):
    return render(request, 'facilities/facilities_overview.html')

#templates / facilities


from .models import Product


def product_detail_view(request):
    obj=Product.objects.get(id=1)
    context={
        'title':obj.title,
        'desc':obj.desc
    }
    # context={'object':obj}
    # then use obj.ttitle and obj.desc in the templates file


    return render(request,"detail.html",context)


from .forms import ProductForm
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

from .forms import RawPrdForm
def product_crea_view1(request):
    mf=RawPrdForm()
    form =RawPrdForm(request.POST)
    if form.is_valid():
        form.save()
        print(request.POST)
        form=RawPrdForm()
        print(request.POST)
    else:
            print form.errors
    context={'form':form}
    return render(request,"create1.html",context)

from .models import NewCustomerReg
def customer_list(request):
    obj=NewCustomerReg.objects.all()
    context={'fobj':obj}
    return render(request,"listCust.html",context)


from .models import RegisterNewEmp
def Staff_list(request):
    obj=RegisterNewEmp.objects.all()
    context={'fobj':obj}
    return render(request,"listStaff.html",context)

#from .models import RegisterNewEmp
from .forms import AddNewEmp
def add_new_Staff(request):
    mf=AddNewEmp()
    form =AddNewEmp(request.POST)
    if form.is_valid():
        form.save()
        print(request.POST)
        form=AddNewEmp()
        print(request.POST)
    else:
            print form.errors
    context={'form':form}
    return render(request,"AddNewStaff.html",context)

from .forms import AddNewFacForm
def Add_new_facility(request):
    mf=AddNewFacForm()
    form =AddNewFacForm(request.POST)
    if form.is_valid():
        form.save()
        print(request.POST)
        form=AddNewFacForm()
        print(request.POST)
    else:
            print form.errors
    context={'form':form}
    return render(request,"AddNewFac.html",context)

from .forms import NewBookingForm
def AddNewBookingFn(request):
    mf=NewBookingForm()
    form =NewBookingForm(request.POST)
    if form.is_valid():
        form.save()
        print(request.POST)
        form=NewBookingForm()
        print(request.POST)
    else:
            print form.errors
    context={'form':form}
    return render(request,"NewBookingForm.html",context)

from .forms import CancelBookingForm
def CancelBookingFn(request):
    mf=CancelBookingForm()
    obj=Bookings.objects.all()
    form =CancelBookingForm(request.POST)
    if request.method == 'POST':
        # form.save()
        instance = Bookings.objects.get(id=request.POST['id'])
        instance.delete()
        print(request.POST)
        form=CancelBookingForm()
        print(request.POST)
    else:
            print form.errors
    context={'form':form,'fobj':obj}
    return render(request,"CancelBookingForm.html",context)


from .models import Bookings
def listBooking(request):
    obj=Bookings.objects.all()
    context={'fobj':obj}
    return render(request,"listBooking.html",context)
