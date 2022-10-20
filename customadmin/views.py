from django.http import HttpResponse
from django.shortcuts import render,redirect


from django.contrib import messages, auth
from psycopg2 import IntegrityError
from accounts.models import User
from django.contrib.auth.decorators import login_required
from customadmin import forms
from marketplace.models import Tax
from .forms import AddTaxForm

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
        context = {'user':user}
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