
from django.conf.urls import url
#from django.contrib import admin
from .import views 

urlpatterns = [
    #url(r'^admin/', admin.site.urls), # admin should be start of the string. ^ means that. $ sign mean s end of the string. 
    url(r'^$', views.facility_overview), # home page # start and end mentioned by carat and dollar consequtively
    #url(r'^about/$', views.about) # about page
]
