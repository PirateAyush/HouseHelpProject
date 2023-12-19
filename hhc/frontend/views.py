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

def  whyUs(request):

    return render(request,'frontend/whyUs.html')