from django.http import HttpResponse
from django.shortcuts import render,redirect


from django.contrib import messages, auth
from accounts.models import User
# Create your views here.
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_index')
    else:
        if request.method == 'POST':
            print('inside post')
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


def admin_index(request):
    if request.user.is_authenticated:
        user = User.objects.all()
        context = {'user':user}
        return render(request, 'customadmin/admin_index.html', context)
    


def admin_logout(request):
    auth.logout(request)
    return redirect('admin_login')


def users(request):
    user = User.objects.all()
    context = {'user':user}
    return render(request, 'customadmin/users.html', context)

def blockuser(request,id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return redirect('admin_index')


def unblock(request,id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return redirect('admin_index')
    

def deleteuser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('admin_index')