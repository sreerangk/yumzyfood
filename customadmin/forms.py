from django import forms
from marketplace.models import Tax
from accounts.models import User
from orders.models import Order,Refund



class AddTaxForm(forms.ModelForm):

    class Meta:
        model = Tax
        fields = ['tax_type','tax_percentage','is_active']
        
        
class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','phone_number','email','first_name','is_active','is_admin','is_staff','is_active',]
        
        
         
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user','payment','vendors','order_number','phone','email','address','city','total','total_tax','payment_method','status','is_ordered',]       

class RefundForm(forms.ModelForm):
    class Meta:
        model = Refund
        fields = ['order','reason','accepted','email',]       