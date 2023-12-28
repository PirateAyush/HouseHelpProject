from django.contrib import admin

# Register your models here.
from .models import CustomeUser

admin.site.register(CustomeUser)