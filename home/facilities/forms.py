from django import forms

from .models import Product
from .models import NewCustomerReg

class ProductForm(forms.ModelForm):
    class Meta:
         model = Product
         fields=['title','desc','price']

# class RawPrdForm(forms.Form):
#     title=forms.CharField(label='this is the lab')
#     desc=forms.CharField()
#     #price=forms.DecimalField()
#     price=forms.CharField()


class RawPrdForm(forms.ModelForm):
    class Meta:
        model = NewCustomerReg
        fields=['CustomerName','title','Address','IDType','IDNumber']
        # CustomerName=forms.CharField()
        # title=forms.CharField()
        # Address=forms.CharField()
        # IDType=forms.CharField()
        # IDNumber=forms.CharField()

