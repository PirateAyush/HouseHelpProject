from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from . import constants

def index(request):

    params = {'services':constants.SERVICES,'userExist':True}
    return render(request,'frontend/index.html',params)

def about(request):

    return render(request,'frontend/about.html')
# Create your views here.

def  user(request):

    return render(request,'frontend/user.html')

def  prices(request):

    return render(request,'frontend/prices.html')

def  basic(request):

    return render(request,'frontend/basic_form.html')

def backgroundVerification(request):
    
    return render(request,'frontend/background_verification_form.html')

def advance(request):
    
    return render(request,'frontend/advance_form.html')