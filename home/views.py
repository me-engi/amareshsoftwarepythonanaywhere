from django.shortcuts import render
from home.models import *
from pricing.models import pricingSection
from about.models import teamSection
from blog.models import *
from settings.models import templateSettings
from analytics.views import visitor_data
# ===============> Front Home Page View <===============

def homePageFront(request):
    visitor_data(request)
    
    meta = homePageSEO.objects.first()
    sliders = sliderSection.objects.all()
    services = serviceSection.objects.all()
    about = aboutSection.objects.first()
    funfacts = funFactSection.objects.all()
    project_categories= projectCategory.objects.all()
    projects = projectSection.objects.all().order_by('?')
    clients = clientSection.objects.all()
    testimonials = testimonialsSection.objects.all()
    pricings = pricingSection.objects.all()
    teams = teamSection.objects.all()
    blogs = Blogs.objects.all().order_by('?')
    
    template_settings = templateSettings.objects.first()
    
    if not template_settings:
        template_settings = templateSettings.objects.create(template1=True)

    context = {
        'meta' : meta,
        'sliders' : sliders,
        'services' : services,
        'about' : about,
        'funfacts' : funfacts,
        'project_categories' : project_categories,
        'projects': projects,
        'clients' : clients,
        'testimonials' : testimonials,
        'pricings' : pricings,
        'teams' : teams,
        'blogs' : blogs,
    }
   
    
    if template_settings.template1 == True:
        return render(request, 'front/main/index.html', context)
    elif template_settings.template2 == True:
        return render(request, 'front/main/home2.html', context)
    else:
        return render(request, 'front/main/index.html', context)

def error_404(request, exception):
    return render(request, 'error/404.html', status=404)