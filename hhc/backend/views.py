from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render

#Models
from .models import *

#Constants
from frontend.constants import *

#Form Imports
from django import forms
from django.contrib.auth import authenticate,login,logout

#Messages
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'backend/index.html')

def whyChooseUs(request):
    return render(request,'backend/why-choose.html')

def aboutUs(request):
    return render(request,'backend/about.html')

def services(request):
    return render(request,'backend/services.html')

def ourTeam(request):
    return render(request,'backend/team.html')

def ourGallery(request):
    return render(request,'backend/gallery.html')

def blogPosts(request):
    return render(request,'backend/news.html')

def addBlogPosts(request):
    return render(request,'backend/news-single.html')

def contact(request):
    return render(request,'backend/contact.html')

def register(request):
    if request.method == 'POST':  
        print(request.POST.dict())
        messages.error(request, 'Registered Successfull !')
        return redirect('Home')

def service(request,service_id):
    service = get_object_or_404(Service,id=service_id)
    params = {'service':service}
    print(service)
    return render(request,'backend/service-info.html',params)

def error_404(request):

    return render(request,'backend/error.html')