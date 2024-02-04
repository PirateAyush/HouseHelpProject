from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'backend'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="Home"),
    path("whyChooseUs", views.whyChooseUs, name="WhyChooseUs"),
    path("aboutUs", views.aboutUs, name="AboutUs"),
    path("services", views.services, name="Services"),
    path("ourTeam", views.ourTeam, name="OurTeam"),
    path("ourGallery", views.ourGallery, name="OurGallery"),
    path("blogPosts", views.blogPosts, name="BlogPosts"),
    path("addBlogPosts/<int:blog_id>", views.addBlogPosts, name="AddBlogPosts"),
    path("contact", views.contact, name="Contact"),
    path("register", views.register, name="Register"),
    path("services/<int:service_id>", views.service, name="Service"),
    path("rate-us", views.rateUs, name="RateUs"),
    path("comment", views.comment, name="Comment"),
    
    #POST LOGIN
    path("login", views.login, name="Login"),
    
    path("error/404",views.error_404,name="Error404"),
]
