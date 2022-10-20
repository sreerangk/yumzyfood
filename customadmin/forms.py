from django import forms

from marketplace.models import Tax





class AddTaxForm(forms.ModelForm):

    class Meta:
        model = Tax
        fields = ['tax_type','tax_percentage','is_active']
        
   