from django.http import HttpResponse
from django.shortcuts import render,redirect


from django.contrib import messages, auth
from accounts.models import User
from django.contrib.auth.decorators import login_required
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
def user_edit(request):
    user = User.objects.all()
    context = {
        'user':user
        }
    return render(request, 'customadmin/user_edit.html', context)

@login_required(login_url='login')
def blockuser(request,id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    messages.success(request, 'blocked user successfully')
    return redirect('user_edit')


@login_required(login_url='login')
def unblock(request,id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    messages.success(request, 'unblocked user successfully')
    return redirect('user_edit')
    

@login_required(login_url='login')
def deleteuser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, 'Delete user successfully')
    return redirect('user_edit')