from django import forms
from .models import Vendor,OpeningHour
from accounts.validators import allow_only_images_validator
from orders.models import Order


class VendorForm(forms.ModelForm):
    vendor_license = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_license']


class OpeningHourForm(forms.ModelForm):
    class Meta:
        model = OpeningHour
        fields = ['day', 'from_hour', 'to_hour', 'is_closed']
        
        

# class OrderStatusform(forms.ModelForm):
#     class Meta:
#         model=Order
#         fields=['status']
#     def __init__(self, *args, **kwargs):
#         super(OrderStatusform, self).__init__(*args, **kwargs)
#         self.fields['status'].widget.attrs.update({'class': 'form-control'})
        
