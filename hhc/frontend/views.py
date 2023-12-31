from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

#Models
from .models import *

#Constants
from .constants import *

#Form Imports
from django import forms
from .forms import CustomeUserForm
from django.contrib.auth import authenticate,login,logout

#Messages
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        first_name         = request.POST.get('fname')
        last_name          = request.POST.get('lname')
        phone_number       = request.POST.get('mobile')
        address            = request.POST.get('address')
        pin                = request.POST.get('pincode')
        email              = request.POST.get('email')
        user_name          = request.POST.get('uname')
        password           = request.POST.get('password')
        reason_for_contact = request.POST.get('reason_for_contact')
        reason             = request.POST.get('reason')
        status             = ACTIVE
        # print(user_name,first_name,last_name,phone_number,address,pin,email,password,reason_for_contact,reason,status)
        custome_user_instance = CustomeUser(user_name=user_name,first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,pin=pin,email=email,password=password,reason=reason_for_contact,reason_text=reason,status=status)
        custome_user_instance.save()
        messages.success(request,"Registration Successful")
        return redirect("Home")

    params = {'services':SERVICES,'userExist':True,}
    return render(request,'frontend/index.html',params)

def about(request):

    return render(request,'frontend/about.html')
# Create your views here.

def  user(request):
    if request.method == "POST":
        username   = request.POST['uname']
        password   = request.POST['password']

        try:
            user = CustomeUser.objects.get(user_name=username, password=password)
        except CustomeUser.DoesNotExist:
            user = None
        if user is not None:
            print(user.id)
            return redirect('userSpecific',user_id=user.id)
        else:
            return redirect("Home")
    else:
        return redirect("Home")

def userSpecific(request,user_id):
    user = get_object_or_404(CustomeUser,id=user_id)
    params = {'user':user}
    return render(request,'frontend/user.html',params)
    

def  prices(request):

    return render(request,'frontend/prices.html')

def  whyUs(request):

    return render(request,'frontend/whyUs.html')

def  basic(request,user_id):

    user = get_object_or_404(CustomeUser,id=user_id)
    params = {'user':user}
    return render(request,'frontend/basic_form.html',params)

def backgroundVerification(request,user_id):

    user = get_object_or_404(CustomeUser,id=user_id)
    params = {'user':user}    
    return render(request,'frontend/background_verification_form.html',params)

def advance(request,user_id):

    user = get_object_or_404(CustomeUser,id=user_id)

    params = {'user':user}    
    return render(request,'frontend/advance_form.html',params)
