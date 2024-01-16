from django.db import models

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