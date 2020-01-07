from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'homePage.html')

    #return HttpResponse('homerPage')

def about (request):
    return render(request,'aboutPage.html')

    #return HttpResponse('babout')

    
def footer (request):
    return render(request,'footer.html')

def social_view_ex (request,*args,**kwargs):
    # return render(request,'footer.html')
    return HttpResponse("<h1>example test social</h1>")


def about_view(request,*args,**kwargs):
    my_context={
        "texter": "this is dummy cont",
        "number": 123,
        "lister":[123,234,345,456,567]
    }
    return render(request,"about1.html",my_context)

