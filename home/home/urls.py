
from django.conf.urls import url,include
from django.contrib import admin
from .import views 

urlpatterns = [
    url(r'^admin/', admin.site.urls), # admin should be start of the string. ^ means that. $ sign mean s end of the string. 
    url(r'^$', views.home), # home page # start and end mentioned by carat and dollar consequtively
    url(r'^home/$', views.home), # home page # start and end mentioned by carat and dollar consequtively
    url(r'^about/$', views.about), # about page
       url(r'^facilities/', include('facilities.urls')), # about page
       url(r'^footer/$', views.footer), # about page
]
