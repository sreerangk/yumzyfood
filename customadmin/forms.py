from django import forms

from marketplace.models import Tax
from vendor.models import Vendor





class AddTaxForm(forms.ModelForm):

    class Meta:
        model = Tax
        fields = ['tax_type','tax_percentage','is_active']
        
        
class VendorForm(forms.ModelForm):
    is_approved = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}))
    class Meta:
        model = Vendor
        fields = ['user','user_profile','vendor_name','vendor_license','is_approved']
   