from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from django.views import View

#Models
from .models import *
from backend.models import CustomeUser

#Constants
from backend.constants import *

#Form Imports
from django import forms
from django.contrib.auth import authenticate,login,logout

#Messages
from django.contrib import messages

#URL Imports
from django.urls import reverse
# Create your views here.
def index(request,user_id):
    request.session['user_id'] =  user_id  #set the session variable for the current logged in user
    try:
        user = CustomeUser.objects.get(id = user_id,)
    except CustomeUser.DoesNotExist:
        user = None
    if user is not None:
        params = {'user':user}
        messages.success(request, 'Login Successfull!')
        return render(request,'dashboard/dashboard.html',params)
    else:
        return redirect("backend:Error404")
    
def profile(request):
    user = CustomeUser.objects.get(id = request.session.get('user_id'))
    params = {'user':user}
    return render(request,'dashboard/build-profile.html',params)
    pass

def advance(request):
    user = CustomeUser.objects.get(id = request.session.get('user_id'))
    params = {'maid':True,'customer':False,'user':user}
    return render(request,'dashboard/advance-profile.html',params)

def verification(request):
    user = CustomeUser.objects.get(id = request.session.get('user_id'))
    params = {'maid':True,'customer':False,'user':user}
    if request.method == 'POST':
        print("-------------------------------------------------------------------")
        print(request.POST.get('adhaar'))
        print("-------------------------------------------------------------------")
    return render(request,'dashboard/verification-profile.html',params)
    pass


