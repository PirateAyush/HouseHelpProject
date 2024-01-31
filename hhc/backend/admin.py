from django.contrib import admin

# Register your models here.
from .models import Service,Feedback,TeamMember,Blog,CustomeUser

admin.site.register(Service)
admin.site.register(Feedback)
admin.site.register(TeamMember)
admin.site.register(Blog)
admin.site.register(CustomeUser)