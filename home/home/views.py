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
