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
    path("advance", views.advance, name="Advance"),
    path("verification", views.verification, name="Verification"),
    path("find-match", views.findMatch, name="FindMatch"),
    path("view-profile/<int:user_id>",views.viewProfile,name="ViewProfile"),
    path("comment", views.comment, name="Comment"),
    path("explore-maids/",views.exploreMaids,name="ExploreMaids"),
    path("explore-customers/",views.exploreCustomers,name="ExploreCustomers"),
    
    
    path("",views.logOut,name="LogOut")
]