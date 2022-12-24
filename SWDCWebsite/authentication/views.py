from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from . models import IsCoord, vdata
import pdb


def index(request):
    return render(request, 'index.html')


def VolunteerRegistrationView(request):
    if request.method == "GET":
        # messages.error(request, 'Oops!! Registrations have closed now!!')
        return render(request, 'vreg.html')
    else:
        name = request.POST['Name']
        email = request.POST['email']
        gender = request.POST['gender']
        activity = request.POST['activity']
        dept = request.POST['dept']
        academic_year = request.POST['year']
        module = request.POST['module']
        div = request.POST['div']
        current_add = request.POST['add']
        prn = request.POST['prn']
        roll = request.POST['roll']
        contact_num = request.POST['number']

        if activity == 'Utkarsh':
            u = vdata.objects.filter(activity='Utkarsh')
            Uc = 0
            for i in u:
                Uc = Uc+1
            if (Uc > 199):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')

        if activity == 'Go Green':
            g = vdata.objects.filter(activity='Go Green')
            Gc = 0
            for i in g:
                Gc = Gc + 1
            if (Gc > 49):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')

        if activity == 'Swaccha Pune':
            s = vdata.objects.filter(activity='Swaccha Pune')
            sc = 0
            for i in s:
                sc = sc + 1
            if (sc > 79):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')

        if activity == 'Night Patroling':
            n = vdata.objects.filter(activity='Night Patroling')
            nc = 0
            for i in n:
                nc = nc + 1
            if (nc > 29):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')

        if activity == 'Matadhikar':
            m = vdata.objects.filter(activity='Matadhikar')
            mc = 0
            for i in m:
                mc = mc + 1
            if (mc > 49):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')
        if activity == 'Praytna':
            p = vdata.objects.filter(activity='Praytna')
            Pc = 0
            for s in p:
                Pc = Pc+1
            if (Pc > 29):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')

        if activity == 'Udaan':
            um = vdata.objects.filter(activity='Udaan', gender='male')
            uf = vdata.objects.filter(activity='Udaan', gender='female')
            umc = 0
            ufc = 0
            for s in um:
                umc = umc+1
            for s in uf:
                ufc = ufc+1
            if gender == 'male':
                if umc > 9:
                    messages.error(
                        request, 'The registrations of boys for this activity is closed now.')
                    return render(request, 'vreg.html')
            if gender == 'female':
                if ufc > 39:
                    messages.error(
                        request, 'The registrations of girls for this activity is closed now.')
                    return render(request, 'vreg.html')

        if activity == 'Umang':
            u = vdata.objects.filter(activity='Umang')
            Uc = 0
            for s in u:
                Uc = Uc+1
            if (Uc > 39):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')

        if activity == 'Vatsalya':
            v = vdata.objects.filter(activity='Vatsalya')
            vc = 0
            for s in v:
                vc = vc+1
            if (vc > 49):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')

        if activity == 'Liliput':
            l = vdata.objects.filter(activity='Liliput')
            lc = 0
            for s in l:
                lc = lc+1
            if (lc > 29):
                messages.error(
                    request, 'The registrations for this activity is closed now.')
                return render(request, 'vreg.html')
        # if activity == 'Muskan':
        #     m = vdata.objects.filter(activity='Muskan')
        #     mc = 0
        #     for s in m:
        #         mc = mc+1
        #     if (mc > 70):
        #         messages.error(
        #             request, 'The registrations for this activity is closed now.')
        #         return render(request, 'vreg.html')
        if User.objects.filter(username=name).exists():
            messages.error(request, 'This name is already registered with us!')
            return redirect('vreg')
        if User.objects.filter(email=email).exists():
            messages.error(
                request, 'This email is already registered with us!')
            return redirect('vreg')
        if vdata.objects.filter(contact_num=contact_num).exists():
            messages.error(
                request, 'This mobile number is already registered with us!')
            return redirect('vreg')
        user = User.objects.create_user(
            username=name, email=email, first_name="volunteer", last_name=gender)
        user.is_active = True
        user.set_password(email)
        user.save()
        reg = vdata.objects.create(owner=user, Name=name, email=email, gender=gender, activity=activity, dept=dept,
                                   academic_year=academic_year, module=module, div=div, current_add=current_add, prn=prn, roll=roll, contact_num=contact_num)
        reg.save()
        messages.success(
            request, 'Your registration for the activity '+activity+' was successfull.')
        return redirect('vreg')


def CoordRegistrationView(request):
    if request.method == "GET":
        return render(request, 'creg.html')
    else:
        name = request.POST['Name']
        email = request.POST['email']
        gender = request.POST['gender']
        dept = request.POST['dept']
        academic_year = request.POST['year']
        module = request.POST['module']
        div = request.POST['div']
        current_add = request.POST['add']
        prn = request.POST['prn']
        roll = request.POST['roll']
        contact_num = request.POST['number']
        user = User.objects.create_user(
            username=name, email=email, first_name="coord", last_name=gender)
        user.set_password(email)
        user.is_active = True
        user.save()
        regi = IsCoord.objects.create(owner=user, cname=name, email=email, gender=gender, dept=dept,
                                      academic_year=academic_year, module=module, div=div, current_add=current_add, prn=prn, roll=roll, contact_num=contact_num)
        regi.save()
        messages.success(
            request, 'Your registration was successfull.')
        return redirect('creg')


def LoginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        CoordUsernames = []
        obj = IsCoord.objects.all()
        for c in obj:
            CoordUsernames.append(c.cname)
        if username and password:
            if username in CoordUsernames:
                user = auth.authenticate(username=username, password=password)
                if user:
                    auth.login(request, user)
                    messages.success(
                        request, 'Welcome '+username+', you have been logged in successfully!')
                    return redirect('CDashboard')
                else:
                    messages.error(request, 'Wrong credentials!')
                    return redirect('login')
            else:
                user = auth.authenticate(username=username, password=password)
                if user:
                    auth.login(request, user)
                    messages.success(
                        request, 'Welcome '+username+', you have been logged in successfully!')
                    return redirect('vdashboard')
                else:
                    messages.error(request, 'Wrong credentials!')
                    return redirect('login')
        else:
            messages.error(request, 'Please fill all fields!')
            return redirect('login')


def LogoutView(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')
    else:
        messages.error(
            request, 'You tried accessing a prohibited url. Don\'t try that again!!')
        return redirect('login')
