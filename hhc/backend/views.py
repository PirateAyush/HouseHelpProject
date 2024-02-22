from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from django.views import View

#Models
from .models import *

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
def index(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    #Feedback Sub-Page Section
    ratings = Feedback.objects.filter(type=FEEDBACK_TYPE_RATE_US, status=ACTIVE, rating__gt=3).order_by('-created_at')[:3]
    blogs = Blog.objects.all()
    params    = {'ratings':ratings, 'blogs':blogs, 'services':services}
    
    return render(request,'backend/index.html',params)

def whyChooseUs(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    params    = {'services':services}
    
    return render(request,'backend/why-choose.html',params)

def aboutUs(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    
    #Team Sub-Page Section
    teamMembers=TeamMember.objects.filter(level=TEAM_MEMBER_LEVEL_HIGH)[:3]
    params    = {'teamMembers':teamMembers, 'services':services}
    
    return render(request,'backend/about.html',params)

def services(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    params    = {'services':services}
    
    return render(request,'backend/services.html',params)

def ourTeam(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    
    #TeamMembers
    teamMembers=TeamMember.objects.filter(level=TEAM_MEMBER_LEVEL_HIGH)[:3]
    params    = {'teamMembers':teamMembers, 'services':services}
    
    return render(request,'backend/team.html',params)

def ourGallery(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    params    = {'services':services}
    
    return render(request,'backend/gallery.html',params)

def blogPosts(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    
    #Blogs
    blogs = Blog.objects.all()
    params = {'blogs':blogs, 'services':services}
    
    return render(request,'backend/news.html',params)

def addBlogPosts(request,blog_id):
    
    services = Service.objects.all()
    blogs    = Blog.objects.all()
    comments = Feedback.objects.filter(type=FEEDBACK_TYPE_COMMENTS, status=ACTIVE, blog_id=blog_id).order_by('-created_at')[:3]

    try:
        blog = get_object_or_404(Blog,id=blog_id)
        params = {'blog':blog,'services':services,'blogs':blogs, 'comments':comments}
        return render(request,'backend/news-single.html',params)
    except Http404:
        return redirect('backend:Error404')

def contact(request):
    #Service Nav-Bar Dynamic
    services = Service.objects.all()
    params    = {'services':services}
    
    return render(request,'backend/contact.html',params)

def register(request):
    if request.method == 'POST': 
        
        first_name         = request.POST.get('form_name')
        last_name          = request.POST.get('form_last_name')
        phone_number       = request.POST.get('form_phn')
        address            = request.POST.get('form_address')
        pin                = request.POST.get('form_pin')
        email              = request.POST.get('form_email')
        user_name          = request.POST.get('form_username')
        password           = request.POST.get('form_password')
        reason             = request.POST.get('reason')
        status             = ACTIVE
        profile            = request.FILES.get('profile_photo')
        
        custome_user_instance = CustomeUser(user_name=user_name,first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,pin=pin,email=email,password=password,reason=reason,profile=profile,status=status)
        custome_user_instance.profile = profile
        custome_user_instance.save()
        
        messages.success(request, 'Registered Successfull !')
        return redirect('backend:Home')

def service(request,service_id):
    try:
        service = get_object_or_404(Service,id=service_id)
        params = {'service':service}
        return render(request,'backend/service-info.html',params)
    except Http404:
        return redirect('backend:Error404')

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
        return redirect("backend:Home")
    
    
    
    return render(request,'backend/feedback.html')
    
def comment(request):

    if request.method == 'POST': 
        full_name = request.POST.get('fname', '')
        split_name = full_name.split()

        first_name  = split_name[0] if split_name else ''
        last_name   = ' '.join(split_name[1:]) if len(split_name) > 1 else ''
        email       = request.POST.get('form_email')
        profile     = request.FILES.get('profile_photo')
        comment     = request.POST.get('message')
        blog_id     = request.POST.get('blog_id')
        type        = FEEDBACK_TYPE_COMMENTS
        status      = ACTIVE
        feedback_instance = Feedback(
                                    first_name = first_name,
                                    last_name  = last_name,
                                    email      = email,
                                    profile    = profile,
                                    comment    = comment,
                                    blog_id    = blog_id,
                                    type       = type,
                                    status     = status
                                )
        feedback_instance.profile = profile
        feedback_instance.save()
        messages.success(request, 'We Received Your Comment!')
        return redirect('backend:AddBlogPosts',blog_id)
        
    else:
        return render(request,'backend/error.html')
    

def login(request):
    if request.method == "POST":
        username   = request.POST['uname']
        password   = request.POST['password']

        try:
            user = CustomeUser.objects.get(user_name=username, password=password)
        except CustomeUser.DoesNotExist:
            user = None
        if user is not None:
            # messages.success(request, 'Login Successfull!')
            return redirect('dashboard:Dashboard',user_id=user.id)
        else:
            messages.error(request, 'Login Failed!')
            return redirect("backend:Home")
    
def error_404(request):

    return render(request,'backend/error.html')