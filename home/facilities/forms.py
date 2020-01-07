from django import forms



from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
         model = Product
         fields=['title','desc','price']

# class RawPrdForm(forms.Form):
#     title=forms.CharField(label='this is the lab')
#     desc=forms.CharField()
#     #price=forms.DecimalField()
#     price=forms.CharField()

from .models import NewCustomerReg
class RawPrdForm(forms.ModelForm):
    class Meta:
        model = NewCustomerReg
        fields=['CustomerName','title','Address','IDType','IDNumber']

from .models import RegisterNewEmp
class AddNewEmp(forms.ModelForm):
    class Meta:
        model = RegisterNewEmp
        fields=['EmpName','IDType','IDNumber','Address','BloodGroup','DOB','Wage','Desc','Designation','SocialSecNo']

from .models import RegisterNewFacility
class AddNewFacForm(forms.ModelForm):
    class Meta:
        model = RegisterNewFacility
        fields=['FacilityName','BuildingNo','Floor','Description','MinorsAllowed']

from .models import Bookings
class NewBookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields=['CustomerName','custID','RoomNo','CheckinDate','CheckOutDate','TotalCost']



