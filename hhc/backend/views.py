from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'backend/index.html')

def whyChooseUs(request):
    return render(request,'backend/why-choose.html')

def aboutUs(request):
    return render(request,'backend/about.html')

def services(request):
    return render(request,'backend/services.html')

def ourTeam(request):
    return render(request,'backend/team.html')

def ourGallery(request):
    return render(request,'backend/gallery.html')

def blogPosts(request):
    return render(request,'backend/news.html')

def addBlogPosts(request):
    return render(request,'backend/news-single.html')

def contact(request):
    return render(request,'backend/contact.html')

