from django.db import models

#CreatedBy UpdatedBy Helper
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
import uuid

#Constant Import
from backend.constants import *

# Create your models here.
class Service(models.Model):
    id            = models.AutoField(primary_key=True)
    service_title = models.CharField(max_length=255)
    service_image = models.ImageField(upload_to='backend/services/images')
    service_description = models.TextField()
    support_image = models.ImageField(upload_to='backend/services/images/support_images')
    support_image2 = models.ImageField(upload_to='backend/services/images/support_images',default="")
    
    additional_content_title_1 = models.CharField(max_length=255,default="")
    additional_content_1       = models.TextField(default="")
    additional_content_title_2 = models.CharField(max_length=255,default="")
    additional_content_2       = models.TextField(default="")
    
    
    def __str__(self):
        return self.service_title
    
class Feedback(models.Model):
    id         = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name  = models.CharField(max_length=255, null=True, blank=True)
    email      = models.EmailField(null=True, blank=True)
    profile    = models.ImageField(upload_to='backend/feedback_and_comments/profiles', null=True, blank=True)
    rating     = models.IntegerField(null=True, blank=True)
    feedback   = models.TextField(null=True, blank=True)
    comment    = models.TextField(null=True, blank=True)
    blog_id    = models.IntegerField(null=True, blank=True, default=-1)
    type       = models.IntegerField(null=True, blank=True) #Type 1 => Feedback ; Type 2 => Comments
    status     = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        if self.type == FEEDBACK_TYPE_COMMENTS:
            type =  "Comment"
        else:
            type = "Feedback"
        
        return f"{self.first_name} {self.last_name} - {type}"

class TeamMember(models.Model):
    id               = models.AutoField(primary_key=True)
    profile          = models.ImageField(upload_to='backend/team_profiles/', blank=True, null=True)
    first_name       = models.CharField(max_length=50)
    last_name        = models.CharField(max_length=50)
    post             = models.CharField(max_length=50)
    facebook_profile = models.URLField(max_length=500, blank=True, null=True)
    twitter_profile  = models.URLField(max_length=500, blank=True, null=True)
    linkedin_profile = models.URLField(max_length=500, blank=True, null=True)
    
    level            = models.IntegerField(null=True, blank=True,default=0)
    
    created_at       = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at       = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.post}"
    
 
class Blog(models.Model):
    id                 = models.AutoField(primary_key=True)
    blog_title         = models.CharField(max_length=255)
    blog_image         = models.ImageField(upload_to='backend/blogs/images')
    blog_description_1 = models.TextField()
    blog_description_2 = models.TextField()
    uploaded_by        = models.CharField(max_length=50)
    created_at         = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at         = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.blog_title} by {self.uploaded_by}"
    
class CustomeUser(models.Model):
    id          = models.AutoField(primary_key=True)
    uuid        = models.UUIDField(default=uuid.uuid4, editable=False)
    user_name   = models.CharField(max_length = 50)
    first_name  = models.CharField(max_length = 50)
    last_name   = models.CharField(max_length = 50)
    phone_number= models.IntegerField(null=True)
    address     = models.CharField(max_length = 300,null=True)
    pin         = models.IntegerField(null=True)
    email       = models.EmailField(unique = True,null=True)
    password    = models.CharField(max_length = 100,null=True)
    reason      = models.IntegerField(null=True)
    profile     = models.ImageField(upload_to='backend/users/profiles', null=True, blank=True)
    status      = models.IntegerField(null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user_name