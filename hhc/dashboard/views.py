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
        print(user)
        messages.success(request, 'Login Successfull!')
        return render(request,'dashboard/dashboard.html',params)
    else:
        return redirect("backend:Error404")
    
def profile(request):
    params = {'user_id':request.session.get('user_id')}
    return render(request,'dashboard/build-profile.html',params)
    pass

def advance(request):
    return render(request,'dashboard/build-profile.html')
    pass

def verification(request):
    return render(request,'dashboard/build-profile.html')
    pass


