from dataclasses import field
from django import forms 
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name', 'phone','email','address','country','state','city','pin_code']
        
class RefundForm(forms.Form):
    order_number = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
    }))   
    email = forms.EmailField() 