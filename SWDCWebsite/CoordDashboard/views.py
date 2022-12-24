from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import vdata
import pdb;

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def CoordDashboardView(request):
    if request.method =='GET':
        data = vdata.objects.filter(submitted=True, Cordinator=request.user.username, verified=False)
        return render(request, 'cdashboard.html', {'data': data})
    else:
        number = request.POST['number']
        volunteer_data = vdata.objects.get(contact_num=number)
        return render(request, 'ViewVolunteer.html', {'volunteer_data':volunteer_data})
        



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def SetpasswordPageView(request):
    if request.method == 'GET':
        return render(request, 'CPassword.html')
    else:
        password = request.POST['password']
        user = User.objects.get(username=request.user.username)
        user.set_password(password)
        user.save()
        messages.success(
            request, 'Your password was changed successfully! Please login again!')
        return redirect('login')


def ApproveVolunteer(request):
    if request.method=='POST':
        number = request.POST['number']
        volunteer = vdata.objects.get(contact_num=number)
        volunteer.verified = True
        volunteer.save()
        messages.success(request, 'Volunteer '+volunteer.Name+' verified successfully!')
        return redirect('CDashboard')
    else:
        return redirect('CDashboard')


  
