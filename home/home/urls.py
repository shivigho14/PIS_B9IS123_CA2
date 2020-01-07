
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin
from .import views 
from facilities.views import product_detail_view
from facilities.views import product_crea_view
from facilities.views import product_crea_view1
from facilities.views import customer_list
from facilities.views import add_new_Staff
from facilities.views import Staff_list
from facilities.views import Add_new_facility
from facilities.views import AddNewBookingFn
from facilities.views import CancelBookingFn
from facilities.views import listBooking
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls), # admin should be start of the string. ^ means that. $ sign mean s end of the string. 
    url(r'^$', views.home), # home page # start and end mentioned by carat and dollar consequtively
    url(r'^home/$', views.home), # home page # start and end mentioned by carat and dollar consequtively
    url(r'^about/$', views.about), # about page
    url(r'^about1/$', views.about_view), #sample test about page
    url(r'^facilities/', include('facilities.urls')), # about page
    url(r'^footer/$', views.footer), # about page
    url(r'^product/',product_detail_view),
    url(r'^create/',product_crea_view),
    url(r'^create1/$',product_crea_view1),
    url(r'^listCust/$',customer_list),
    url(r'^addNewStaff/$',add_new_Staff),
    url(r'^listStaff/$',Staff_list),
    url(r'^AddNewFac/$',Add_new_facility),
    url(r'^NewBooking/$',AddNewBookingFn),
    url(r'^CancelBooking/$',CancelBookingFn),
    url(r'^listBooking/$',listBooking),
    

    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
