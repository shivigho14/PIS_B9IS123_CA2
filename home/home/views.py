from django.http import HttpResponse

def home(request):
    return HttpResponse('homerPage')

def about (request):
    return HttpResponse('babout')