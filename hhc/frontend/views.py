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
