from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'dashboard'

urlpatterns = [
    #POST LOGIN
    path("<int:user_id>", views.index, name="Dashboard"),
    path("profile", views.profile, name="Profile"),
]