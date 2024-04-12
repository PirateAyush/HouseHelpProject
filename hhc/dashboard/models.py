from django.db import models

# Create your models here.


class UserExtraDetail(models.Model):
    id         = models.AutoField(primary_key=True)
    user_id    = models.IntegerField(null=True)
    user_name  = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50)
    last_name  = models.CharField(max_length = 50)
    
    gender         = models.IntegerField(null=True)
    birth_date     = models.DateField(null=True, blank=True)
    prefered_lang  = models.CharField(max_length = 50)
    
    service_type        = models.JSONField(default=list,null=True,blank=True)
    available_days      = models.JSONField(default=list,null=True,blank=True)
    working_hours       = models.IntegerField(null=True)
    working_hours_from  = models.TimeField(null=True)
    working_hours_to    = models.TimeField(null=True)
    years_of_experience = models.IntegerField(null=True)
    skill_description   = models.TextField(null=True)
    reference_contact   = models.CharField(max_length=20)
    previous_salary     = models.IntegerField(null=True)
    expected_salary     = models.IntegerField(null=True)
    
    adhar_card  = models.ImageField(upload_to='dashboard/users/documents/adhar', null=True, blank=True)
    voting_card = models.ImageField(upload_to='dashboard/users/documents/voting',null=True, blank=True)
    
    profile_build_level = models.IntegerField(default=0,null=True)
    is_verified         = models.BooleanField(default=False,null=True)
    user_type           = models.IntegerField(null=True)
    
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user_name}_{self.id}"