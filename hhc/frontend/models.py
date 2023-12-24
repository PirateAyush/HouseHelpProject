from django.db import models

class CustomeUser(models.Model):
    id          = models.AutoField(primary_key=True)
    user_name   = models.CharField(max_length = 50)
    first_name  = models.CharField(max_length = 50)
    last_name   = models.CharField(max_length = 50)
    phone_number= models.IntegerField(null=True)
    address     = models.CharField(max_length = 300,null=True)
    pin         = models.IntegerField(null=True)
    email       = models.EmailField(unique = True,null=True)
    password    = models.CharField(max_length = 100,null=True)
    reason      = models.IntegerField(null=True)
    status      = models.IntegerField(null=True)
    reason_text = models.CharField(max_length = 300,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
# Create your models here.
    def __str__(self):
        return self.user_name