from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index, name="Home"),
    path("whyChooseUs",views.whyChooseUs, name="WhyChooseUs"),
    path("aboutUs",views.aboutUs, name="AboutUs"),
    path("services",views.services, name="Services"),
    path("ourTeam",views.ourTeam, name="OurTeam"),
    path("ourGallery",views.ourGallery, name="OurGallery"),
    path("blogPosts",views.blogPosts, name="BlogPosts"),
    path("addBlogPosts",views.addBlogPosts, name="AddBlogPosts"),
    path("contact",views.contact, name="Contact"),
]
