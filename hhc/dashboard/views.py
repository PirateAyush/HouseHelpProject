from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render
from django.views import View

#Models
from .models import *
from backend.models import CustomeUser,Feedback,Service,Blog
from django.db.models import Q

#Constants
from dashboard.constants import *
from backend.constants import  *

#Form Imports
from django import forms
from django.contrib.auth import authenticate,login,logout

#Messages
from django.contrib import messages

#URL Imports
from django.urls import reverse

#Date Time Imports
from datetime import time

#JSON Imports
import json

#Arithmetic Imports
import random

# Mail Imports
from django.core.mail import send_mail

# Session Imports
from django.contrib.sessions.models import Session

# Create your views here.
def index(request,user_id):
    request.session['user_id'] =  user_id  #set the session variable for the current logged in user
    try:
        user = CustomeUser.objects.get(id = user_id,)
    except CustomeUser.DoesNotExist:
        user = None
        
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = user_id,)
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        profile_build_level = 0
    if user is not None:
        params = {'user':user,'profile_build_level':profile_build_level}
        # messages.success(request, 'Login Successfull!')
        return render(request,'dashboard/dashboard.html',params)
    else:
        return redirect("backend:Error404")
    
def profile(request):
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = request.session.get('user_id'))
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        profile_build_level = 0
        
    if request.method == 'POST':
        user_id            = request.POST.get('user_id')
        user_type          = request.POST.get('user_type') 
        user_name          = request.POST.get('uname')
        first_name         = request.POST.get('fname')
        last_name          = request.POST.get('lname')
        phone_number       = request.POST.get('phone')
        address            = request.POST.get('address')
        email              = request.POST.get('email')
        gender             = request.POST.get('gender')
        birth_date         = request.POST.get('birth_date')
        language           = request.POST.get('language')
        profile_build_level= PROFILE_BUILD_LEVEL_BASIC
        
        
        customeUserInstance = CustomeUser.objects.get(id = user_id)
        customeUserInstance.first_name   = first_name
        customeUserInstance.last_name    = last_name
        customeUserInstance.email        = email
        customeUserInstance.phone_number = phone_number
        customeUserInstance.address      = address
        customeUserInstance.reason       = user_type
        customeUserInstance.save()
        
        user_exists = UserExtraDetail.objects.filter(user_id=user_id).exists()
        if user_exists:
            userExtraDetail =  UserExtraDetail.objects.get(user_id=user_id)
            userExtraDetail.user_name  = user_name
            userExtraDetail.first_name = first_name
            userExtraDetail.last_name  = last_name
            
            userExtraDetail.gender        = gender
            userExtraDetail.birth_date    = birth_date
            userExtraDetail.prefered_lang = language
            
            userExtraDetail.user_type     = user_type
            
            userExtraDetail.save()
            
            messages.success(request, 'Update Successfully !')
            
            return redirect('dashboard:Profile')
        else:
            userExtraDetailInstance = UserExtraDetail(
                user_id    = user_id,
                user_name  = user_name,
                first_name = first_name,
                last_name  = last_name,
                
                gender         = gender,
                birth_date     = birth_date,
                prefered_lang  = language,
                
                profile_build_level = profile_build_level,
                user_type           = user_type
            )
            userExtraDetailInstance.save()
            messages.success(request, 'Build Successfully ! Proceed with Advance Tab')
            return redirect('dashboard:Advance')
        
    user = CustomeUser.objects.get(id = request.session.get('user_id'))
    try:
        extraUser =  UserExtraDetail.objects.get(user_id = request.session.get('user_id'))
        extraUser.birth_date = extraUser.birth_date.strftime('%Y-%m-%d')
        params = {'user':user, 'profile_build_level':profile_build_level, 'extraUser':extraUser}
        return render(request,'dashboard/build-profile.html',params)
    except UserExtraDetail.DoesNotExist:
        extraUser = {'gender':False, 'prefered_lang':False, 'birth_date':False }
        params = {'user':user, 'profile_build_level':profile_build_level, 'extraUser':extraUser}
        return render(request,'dashboard/build-profile.html',params)

def advance(request):
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = request.session.get('user_id'))
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        messages.error(request, 'Proceed with Profile Tab First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))
    
    if profile_build_level < PROFILE_BUILD_LEVEL_BASIC:
        messages.error(request, 'Complete Profile First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))
    
    if request.method == 'POST':
        if request.POST.get('from') == "" or request.POST.get('to') == "":
            messages.error(request, 'Fill From and To')
            return redirect('dashboard:Advance')
        
        service_type   = json.dumps(request.POST.getlist('service_chekcbox'))
        available_days = json.dumps(request.POST.getlist('chekcboxDay'))
        working_hours  = request.POST.get('working_hours')
        from_hour = int(request.POST.get('from'))
        from_ampm = request.POST.get('from_ampm')
        to_hour = int(request.POST.get('to'))
        to_ampm = request.POST.get('to_ampm')
        
        # Convert the working hours to 24-hour format
        if from_ampm == 'PM' and from_hour != 12:
            from_hour += 12  # Add 12 hours if PM
        elif from_ampm == 'AM' and from_hour == 12:
            from_hour = 0  # Special case for 12 AM

        if to_ampm == 'PM' and to_hour != 12:
            to_hour += 12  # Add 12 hours if PM
        elif to_ampm == 'AM' and to_hour == 12:
            to_hour = 0  # Special case for 12 AM

        # Construct time objects for working hours
        working_hours_from = time(hour=from_hour, minute=0)
        working_hours_to = time(hour=to_hour, minute=0)

        
        years_of_experience = request.POST.get('years_of_exp')
        skill_description   = request.POST.get('skill_desc')
        reference_contact   = request.POST.get('reference_contact')
        previous_salary     = request.POST.get('prev_salary')
        expected_salary     =request.POST.get('expected_salary')
        
        user_exists = UserExtraDetail.objects.filter(user_id=request.session.get('user_id')).exists()
        if user_exists:
            userExtraDetail =  UserExtraDetail.objects.get(user_id=request.session.get('user_id'))
            userExtraDetail.service_type        = service_type
            userExtraDetail.available_days      = available_days
            userExtraDetail.working_hours       = working_hours
            userExtraDetail.working_hours_from  = working_hours_from
            userExtraDetail.working_hours_to    = working_hours_to
            userExtraDetail.years_of_experience = years_of_experience
            userExtraDetail.skill_description   = skill_description
            userExtraDetail.reference_contact   = reference_contact
            userExtraDetail.previous_salary     = previous_salary
            userExtraDetail.expected_salary     = expected_salary
            userExtraDetail.profile_build_level = PROFILE_BUILD_LEVEL_ADVANCE
            userExtraDetail.save()
            
            messages.success(request, 'Build Successfully ! Proceed with Verification Tab')
            return redirect('dashboard:Verification')
        
        else:
            
            messages.error(request, 'Something went wrong! Proceed with  Registration again')
            return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))
    
    
    user        = CustomeUser.objects.get(id = request.session.get('user_id'))
    user_exists = UserExtraDetail.objects.filter(user_id=request.session.get('user_id')).exists()
    
    if user_exists:
        userExtraDetails = UserExtraDetail.objects.get(user_id =  request.session.get('user_id'))
    
    params = {'user_type':user.reason,'user':user, 'userExtraDetails':userExtraDetails, 'profile_build_level':profile_build_level}
    return render(request,'dashboard/advance-profile.html',params)

def verification(request):
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = request.session.get('user_id'))
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        messages.error(request, 'Proceed with Profile Tab First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))

    if profile_build_level < PROFILE_BUILD_LEVEL_ADVANCE:
        messages.error(request, 'Complete Profile First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))
    
    if request.method == 'POST':
        user_exists = UserExtraDetail.objects.filter(user_id=request.session.get('user_id')).exists()
        if user_exists:
            userExtraDetail             =  UserExtraDetail.objects.get(user_id=request.session.get('user_id'))
            userExtraDetail.adhar_card  = request.FILES.get('adhaar')
            userExtraDetail.voting_card = request.FILES.get('voting')
            userExtraDetail.profile_build_level = PROFILE_BUILD_LEVEL_VERIFICATION
            userExtraDetail.save()
            
            messages.success(request, 'Profile is proceed for verification')
            return redirect('dashboard:Verification')
        
        else:
            
            messages.error(request, 'Something went wrong! Proceed with  Registration again')
            return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))
        
    user = CustomeUser.objects.get(id = request.session.get('user_id'))
    
    params = {'maid':True,'customer':False,'user':user, 'profile_build_level':profile_build_level}
    return render(request,'dashboard/verification-profile.html',params)

def findMatch(request):
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = request.session.get('user_id'))
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        messages.error(request, 'Proceed with Profile Tab First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))

    if profile_build_level < PROFILE_BUILD_LEVEL_VERIFICATION:
        messages.error(request, 'Complete Profile First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))

    user = CustomeUser.objects.get(id = request.session.get('user_id'))
    userExtraDetails = UserExtraDetail.objects.get(user_id =  request.session.get('user_id'))

    if user.reason == USER_TYPE_MAID:
        listingUser      = CustomeUser.objects.filter(reason = USER_TYPE_CUSTOMER)
        listingUserExtra = UserExtraDetail.objects.filter(user_type = USER_TYPE_CUSTOMER)
        combined_data = CustomeUser.objects.filter(
            id__in=UserExtraDetail.objects.values('user_id'),
            reason=USER_TYPE_CUSTOMER,  
        )
    else:
        listingUser      = CustomeUser.objects.filter(reason = USER_TYPE_MAID)
        listingUserExtra = UserExtraDetail.objects.filter(user_type = USER_TYPE_MAID)
        combined_data = CustomeUser.objects.filter(
            id__in=UserExtraDetail.objects.filter(prefered_lang = userExtraDetails.prefered_lang).values('user_id'),
            reason=USER_TYPE_MAID, 
        )
    
    for user_extra_detail in combined_data:
        user_extra_detail.extrainfo = UserExtraDetail.objects.get(user_id=user_extra_detail.id)
        jsonDumps = json.dumps(user_extra_detail.extrainfo.service_type)
        user_extra_detail.extrainfo.service_type = json.loads(jsonDumps)
        user_extra_detail.random_rating = random.uniform(3, 5.0)

    params = {'user':user,'userExtraDetails':userExtraDetails,'profile_build_level':profile_build_level,'listingUser':listingUser,'listingUserExtra':listingUserExtra, 'combined_data':combined_data}
    return render(request,'dashboard/find-match.html',params)


def viewProfile(request,user_id):
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = request.session.get('user_id'))
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        messages.error(request, 'Proceed with Profile Tab First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))
    
    if profile_build_level < PROFILE_BUILD_LEVEL_BASIC:
        messages.error(request, 'Complete Profile First')
        return redirect('dashboard:Dashboard',user_id = request.session.get('user_id'))
    
    user        = CustomeUser.objects.get(id = request.session.get('user_id'))
    user_exists = UserExtraDetail.objects.filter(user_id=request.session.get('user_id')).exists()
    
    if user_exists:
        userExtraDetails = UserExtraDetail.objects.get(user_id =  request.session.get('user_id'))
    
    user_profile         = CustomeUser.objects.get(id = user_id)
    user_profile_details = UserExtraDetail.objects.get(user_id = user_id)
    
    service_type_arr =  json.loads(user_profile_details.service_type)
    services = []
    user_profile_details.days_available = ""
    
    own_service_type_arr =  json.loads(userExtraDetails.service_type)
    own_services = []
    
    for i in own_service_type_arr:
        if i == '1':
            own_services.append('Cleaning')
        if i == '2':
            own_services.append('Cooking')
        if i == '3':
            own_services.append('Laundry & Washing')
        if i == '4':
            own_services.append('Baby Sitting')
    
    for i in service_type_arr:
        if i == '1':
            services.append('Cleaning')
        if i == '2':
            services.append('Cooking')
        if i == '3':
            services.append('Laundry & Washing')
        if i == '4':
            services.append('Baby Sitting')
            
    for i in user_profile_details.available_days:
        if i == 'Monday':
            user_profile_details.days_available += "Monday "             
        if i == 'Tuesday':
            user_profile_details.days_available += "Tuesday "             
        if i == 'Wednesday':
            user_profile_details.days_available += "Wednesday "             
        if i == 'Thursday':
            user_profile_details.days_available += "Thursday "             
        if i == 'Friday':
            user_profile_details.days_available += "Friday "             
        if i == 'Saturday':
            user_profile_details.days_available += "Saturday "              
        if i == 'Sunday':
            user_profile_details.days_available += "Sunday " 
    
    if user_profile_details.gender == 1:
        user_profile_details.sex = 'Male'
    elif user_profile_details.gender == 2:
        user_profile_details.sex = 'Female'
    elif user_profile_details.gender == 3:
        user_profile_details.sex = 'Other'
    else:
        user_profile_details.sex = ''
    
    user_profile_details.services = services
    user_profile_details.random_rating = random.uniform(3, 5.0)
    
    
    first_paragraph = f"My name is {user_profile_details.first_name} {user_profile_details.last_name}. I am a {user_profile_details.sex} with {user_profile_details.years_of_experience} years of experience in the {', '.join(user_profile_details.services)} industry. "
    if user_profile_details.skill_description:
        first_paragraph += f"I specialize in {user_profile_details.skill_description}. "

        first_paragraph += f"I am fluent in {user_profile_details.prefered_lang} and am available to work on {', '.join(user_profile_details.days_available)}. "
    first_paragraph +=  "\n\n"
    second_paragraph = f"I have previously worked at {user_profile.address} where I earned {user_profile_details.previous_salary} as my salary. "

    if user_profile_details.reference_contact:
        second_paragraph += f"You can reach out to me at {user_profile_details.reference_contact} for further information. "
        second_paragraph += "I am looking forward to contributing my skills and expertise to your esteemed organization."

    Match = 0
    if userExtraDetails.prefered_lang == user_profile_details.prefered_lang:
        Match += 1
    if own_services.sort() == services.sort():
        Match += 1
    if userExtraDetails.working_hours <= user_profile_details.working_hours:
        Match += 1
    # if userExtraDetails.working_hours_from <= user_profile_details.working_hours_to and userExtraDetails.working_hours_to >= user_profile_details.prefered_lang:
    #     Match += 1
    if userExtraDetails.years_of_experience -1 >= user_profile_details.years_of_experience:
        Match += 1
    if userExtraDetails.expected_salary - 1000 >=  user_profile_details.expected_salary or userExtraDetails.expected_salary + 1000 <=  user_profile_details.expected_salary :
        Match += 1
    
    match_percentage = (Match/5) * 100
    recommendation_percentage = random.uniform(90, 100)
    comments = Feedback.objects.filter(type=3, status=1, blog_id=user_id).order_by('-created_at')[:3]

    params = {'user_type':user.reason,'user':user, 'userExtraDetails':userExtraDetails, 'profile_build_level':profile_build_level, 
              'user_profile':user_profile, 'user_profile_details':user_profile_details, 'first_paragraph':first_paragraph, 
              'second_paragraph':second_paragraph, 'match_percentage':match_percentage, 'recommendation_percentage':recommendation_percentage,
              'comments':comments}
    
    return render(request,'dashboard/view-profile.html',params)


def comment(request):

    if request.method == 'POST': 
        full_name = request.POST.get('name', '')
        split_name = full_name.split()

        first_name  = split_name[0] if split_name else ''
        last_name   = ' '.join(split_name[1:]) if len(split_name) > 1 else ''
        comment     = request.POST.get('message')
        feedback    = request.POST.get('reviewtitle')
        blog_id     = request.POST.get('user_id')
        type        = FEEDBACK_TYPE_MAID_CUSTOMER
        rating     = request.POST.get('rating')
        status      = ACTIVE
        feedback_instance = Feedback(
                                    first_name = first_name,
                                    last_name  = last_name,
                                    comment    = comment,
                                    feedback   = feedback,
                                    blog_id    = blog_id,
                                    rating     = rating,
                                    type       = type,
                                    status     = status
                                )
        feedback_instance.save()
        messages.success(request, 'We Received Your Comment!')
        return redirect('dashboard:ViewProfile',blog_id)
        
    else:
        return render(request,'backend/error.html')

def exploreMaids(request):
    try:
        user = CustomeUser.objects.get(id = request.session.get('user_id'),)
    except CustomeUser.DoesNotExist:
        user = None
        
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = request.session.get('user_id'),)
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        profile_build_level = 0
    
    maids = CustomeUser.objects.filter(reason = 2)
    for maid in maids:
        maid.rating = random.uniform(3, 5)
    
    if user is not None:
        params = {'user':user,'profile_build_level':profile_build_level, 'maids':maids}
        # messages.success(request, 'Login Successfull!')
        return render(request,'dashboard/exploreMaids.html',params)
    else:
        return redirect("backend:Error404")
    
    
def exploreCustomers(request):
    try:
        user = CustomeUser.objects.get(id = request.session.get('user_id'),)
    except CustomeUser.DoesNotExist:
        user = None
        
    try:
        userExtraDetail = UserExtraDetail.objects.get(user_id = request.session.get('user_id'),)
        profile_build_level = userExtraDetail.profile_build_level
    except UserExtraDetail.DoesNotExist:
        profile_build_level = 0
    
    customers = CustomeUser.objects.filter(reason = 1)
    for customer in customers:
        customer.rating = random.uniform(3, 5)
    
    if user is not None:
        params = {'user':user,'profile_build_level':profile_build_level, 'customers':customers}
        # messages.success(request, 'Login Successfull!')
        return render(request,'dashboard/exploreCustomers.html',params)
    else:
        return redirect("backend:Error404")
    
    
def logOut(request):
    services = Service.objects.all()
    ratings = Feedback.objects.filter(type=FEEDBACK_TYPE_RATE_US, status=ACTIVE, rating__gt=3).order_by('-created_at')[:3]
    blogs   = Blog.objects.all()
    params  = {'ratings':ratings, 'blogs':blogs, 'services':services}
    sessions = Session.objects.all()
    sessions.delete()
    return render(request,'backend/index.html',params)
    
    