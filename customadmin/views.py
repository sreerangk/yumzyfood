from contextvars import Context
import profile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect


from django.contrib import messages, auth
from psycopg2 import IntegrityError
from accounts.forms import UserProfileForm
from accounts.models import User, UserProfile
from django.contrib.auth.decorators import login_required
from customadmin import forms
from marketplace.models import Tax
from orders.models import Order
import vendor
from vendor.forms import VendorForm
from vendor.models import Vendor
from .forms import AddTaxForm, UserForm

from django.contrib.auth.decorators import user_passes_test


# Create your views here.
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_index')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(email=email, password=password)
            #print(user.is_admin)
            if user is not None:
                if user.is_superadmin:
                    auth.login(request, user)
                    return redirect('admin_index')
                else:
                    messages.info(request, 'no admin previlages')
                    return redirect('admin_login')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('admin_login')
        else:
            
            return render(request, 'customadmin/admin_login.html')
        #return render(request, 'customadmin/login.html')

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def admin_index(request):
    if request.user.is_authenticated:
        user = User.objects.all()
        context = {
            'user':user
            }
        return render(request, 'customadmin/admin_index.html', context)
    else:
        return redirect('admin_login')
    


@login_required(login_url='login')
def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def user_edit(request):
    user = User.objects.all()
    context = {
        'user':user
        }
    return render(request, 'customadmin/user_edit.html', context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def blockuser(request,id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    messages.success(request, 'blocked user successfully')
    return redirect('user_edit')


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def unblock(request,id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    messages.success(request, 'unblocked user successfully')
    return redirect('user_edit')
    

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def deleteuser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, 'Delete user successfully')
    return redirect('user_edit')


@user_passes_test(lambda u: u.is_superadmin)
def edituser_single(request,id): 

    profile = User.objects.get(id=id)
    form=UserForm(instance=profile)
    context = {
        'form':form,
    }
    try:
        if request.method=='POST':
            form=UserForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'updated success fully')
                return render(request, 'customadmin/edituser_single.html',context)
    except:    
        messages.error(request, 'somthing wrong please check again')
        return redirect('edituser_single')
    
  
    return render(request, 'customadmin/edituser_single.html',context)
# --------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def tax_add(request):
    if request.method == 'POST':
        form=AddTaxForm(request.POST)
        try:
            if form.is_valid():
                tax_type = form.cleaned_data['tax_type']
                tax_percentage = form.cleaned_data['tax_percentage']
                is_active = form.cleaned_data['is_active']
                tax = Tax.objects.create(tax_type=tax_type, tax_percentage=tax_percentage, is_active=is_active)
            
                
                tax.save()
                messages.success(request, 'Tax adedd succesfully!')
                return redirect('tax_add')
        except IntegrityError as e:    
            messages.error(request, 'tax name already exists!')
            return redirect('tax_add')
    else:
        form = AddTaxForm
    context = {
        'form': form,
    }
    
    return render(request, 'customadmin/tax_add.html',context)

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def tax_edit(request):
    tax = Tax.objects.all()
    context = {
        'tax':tax,
    }
    return render(request, 'customadmin/tax_edit.html',context)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def tax_delete(request,id):
    tax = Tax.objects.get(id=id)
    tax.delete()
    messages.success(request, 'Delete user successfully')
    return redirect('tax_edit')

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def order_details(request):
    if request.user.is_authenticated:
        order = Order.objects.all()
        context = {'order':order}
        return render(request, 'customadmin/order_details.html',context)
    else:
        return redirect('admin_login')
   
   
   
# ------------------------------vendorApproval----------------------------

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def vendor_approval(request):
    if request.user.is_authenticated:
        vendor = Vendor.objects.all()
        context = {
            'vendor':vendor,
            
        }
        return render(request, 'customadmin/vendor_approval.html',context)
    else:
        return redirect('admin_index')
    
    
@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin) 
def vendor_profile(request,id):
    if request.user.is_authenticated:
        vendor = Vendor.objects.get(id=id)
        form=VendorForm(request.POST, request.FILES,instance=vendor)
        try:
            if form.is_valid():
                user = form.cleaned_data['user']
                vendor_name = form.cleaned_data['vendor_name']
                vendor_license = form.cleaned_data['vendor_license']
                
                is_approved = form.cleaned_data['is_approved']
                vendor = Vendor.objects.create(vendor_licens=vendor_license,user=user,vendor_name=vendor_name,is_approved=is_approved)
            
                
                vendor.save()
              
                return redirect('vendor_profile')
        except:
            messages.error(request, 'tax name already exists!')
            return redirect('vendor_profile')
    else:
        form=VendorForm(instance=vendor)
    context = {
        'form': form,
     
        'vendor':vendor,
        
    }
     
    return render(request,'customadmin/vendor_profile.html',context)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def activate_vendor(request,id):
    vendor = Vendor.objects.get(id=id)
    vendor.is_approved = True
    vendor.save()
    messages.success(request, 'approved vendor successfully')
    return redirect('vendor_approval')


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superadmin)
def deactivate_vendor(request,id):
    vendor = Vendor.objects.get(id=id)
    vendor.is_approved = False
    vendor.save()
    messages.success(request, 'Denied vendor successfully')
    return redirect('vendor_approval')