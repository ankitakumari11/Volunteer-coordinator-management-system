from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication/index')
def DefaultView(request):
    return redirect ('index')