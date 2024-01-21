from django.contrib import admin

# Register your models here.
from .models import Service,Feedback,TeamMember

admin.site.register(Service)
admin.site.register(Feedback)
admin.site.register(TeamMember)