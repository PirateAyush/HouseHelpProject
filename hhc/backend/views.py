from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse,Http404
from django.shortcuts import render

#Models
from .models import *

#Constants
from backend.constants import *

#Form Imports
from django import forms
from django.contrib.auth import authenticate,login,logout

#Messages
from django.contrib import messages

# Create your views here.
def index(request):
    
    
    #Feedback Sub-Page Section
    ratings = Feedback.objects.filter(type=FEEDBACK_TYPE_RATE_US, status=ACTIVE, rating__gt=3).order_by('-created_at')[:3]
    params    = {'ratings':ratings}
    return render(request,'backend/index.html',params)

def whyChooseUs(request):
    return render(request,'backend/why-choose.html')

def aboutUs(request):
    
    #Team Sub-Page Section
    teamMembers=TeamMember.objects.filter(level=TEAM_MEMBER_LEVEL_HIGH)[:3]
    params    = {'teamMembers':teamMembers}
    return render(request,'backend/about.html',params)

def services(request):
    return render(request,'backend/services.html')

def ourTeam(request):
    
    #TeamMembers
    teamMembers=TeamMember.objects.filter(level=TEAM_MEMBER_LEVEL_HIGH)[:3]
    params    = {'teamMembers':teamMembers}
    return render(request,'backend/team.html',params)

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
    try:
        service = get_object_or_404(Service,id=service_id)
        params = {'service':service}
        return render(request,'backend/service-info.html',params)
    except Http404:
        return redirect('Error404')

def rateUs(request):
    
    if request.method == 'POST':
        full_name = request.POST.get('name', '')
        split_name = full_name.split()

        first_name = split_name[0] if split_name else ''
        last_name  = ' '.join(split_name[1:]) if len(split_name) > 1 else ''
        email      = request.POST.get('email')
        profile    = request.FILES.get('profile_photo')
        feedback   = request.POST.get('feedback')
        rating     = request.POST.get('rating')
        type       = FEEDBACK_TYPE_RATE_US
        status     = ACTIVE
        feedback_instance = Feedback(
                                    first_name = first_name,
                                    last_name  = last_name,
                                    email      = email,
                                    profile    = profile,
                                    feedback   = feedback,
                                    rating     = rating,
                                    type       = type,
                                    status     = status
                                )
        feedback_instance.profile = profile
        feedback_instance.save()
        messages.info(request,"Thank You So Much For The Feedback!")
        return redirect("Home")
    
    
    
    return render(request,'backend/feedback.html')
    

def error_404(request):

    return render(request,'backend/error.html')