from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.shortcuts import render

#Models
from .models import *

#Constants
from .constants import *

#Form Imports
from django import forms
from .forms import CustomeUserForm

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

    return render(request,'frontend/user.html')

def  prices(request):

    return render(request,'frontend/prices.html')

def  whyUs(request):

    return render(request,'frontend/whyUs.html')
def  basic(request):

    return render(request,'frontend/basic_form.html')

def backgroundVerification(request):
    
    return render(request,'frontend/background_verification_form.html')

def advance(request):
    
    return render(request,'frontend/advance_form.html')
