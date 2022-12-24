from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.models import IsCoord, vdata
import pdb


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def VDashboardView(request):
    if request.method == "GET":
        obj = vdata.objects.get(owner=request.user)
        coord = IsCoord.objects.all()
        return render(request, 'vdashboard.html', {'coord': coord, 'obj': obj})
    if request.method == 'POST':
        obj = vdata.objects.get(owner=request.user)
        obj.Objective_of_the_Activity = request.POST['quest1']
        obj.Description_of_the_Activity = request.POST['quest2']
        obj.Benefits_to_Society = request.POST['quest3']
        obj.Benefits_to_Self = request.POST['quest4']
        obj.Learning_Experiences_challenges = request.POST['quest5']
        obj.How_did_it_help_you_to_shape_your_Empathy = request.POST['quest6']
        obj.url = request.POST['quest7']
        obj.Cordinator = request.POST['Cord']
        obj.submitted = True
        obj.save()
        # number = request.POST['number']
        # volunteer_data = vdata.objects.get(contact_num=number)
        # messages.success(request, 'Your Form has been submitted.')
        # return render(request, 'messages.html', {'obj': obj})
        messages.success(request, 'Your Form has been submitted.')
        return render(request, 'vdashboard.html', {'obj': obj})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login')
def SetpasswordPageView(request):
    if request.method == 'GET':
        voldata = vdata.objects.get(owner=request.user)
        return render(request, 'VPassword.html', {'volunteer': voldata})
    else:
        user = User.objects.get(username=request.user.username)
        user.set_password(request.POST['password'])
        vol = vdata.objects.get(owner=request.user)
        vol.Name = request.POST['username']
        vol.contact_num = request.POST['num']
        vol.email = request.POST['email_id']
        vol.prn = request.POST['prn_num']
        user.save()
        vol.save()
        messages.success(
            request, 'Your Credentials have been changed successfully! Please login again!')
        return redirect('login')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(login_url='/login')
# def SetNamePageView(request):
#     if request.method == 'GET':
#         return render(request, 'VPassword.html')
#     else:
#         vol = vdata.objects.get(owner=request.user)
#         vol.Name(request.POST['Name'])
#         vol.save()

#         messages.success(
#             request, 'Your Name was changed successfully! Please login again!')
#         return redirect('login')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(login_url='/login')
# def SetNumberPageView(request):
#     if request.method == 'GET':
#         return render(request, 'VPassword.html')
#     else:
#         vol = vdata.objects.get(owner=request.user)
#         vol.contact_num(request.POST['number'])
#         vol.save()

#         messages.success(
#             request, 'Your Number was changed successfully! Please login again!')
#         return redirect('login')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(login_url='/login')
# def SetEmailPageView(request):
#     if request.method == 'GET':
#         return render(request, 'VPassword.html')
#     else:
#         vol = vdata.objects.get(owner=request.user)
#         vol.email(request.POST['email'])
#         vol.save()

#         messages.success(
#             request, 'Your Email was changed successfully! Please login again!')
#         return redirect('login')


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required(login_url='/login')
# def SetNamePageView(request):
#     if request.method == 'GET':
#         return render(request, 'VPassword.html')
#     else:
#         vol = vdata.objects.get(owner=request.user)
#         vol.prn(request.POST['prn'])
#         vol.save()

#         messages.success(
#             request, 'Your Prn was changed successfully! Please login again!')
#         return redirect('login')
