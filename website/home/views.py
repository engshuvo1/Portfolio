from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *


# Create your views here.

def home (request):
    return render (request,'website/home.html')

def base (request):
    return render (request,'website/base.html')

def Contact (request):
    forms = Contactforms()
    if request.method =='POST':
        forms = Contactforms(request.POST)
       
        forms.save()
        messages.success(request,'successfully-submit')

        # return redirect('Contact')


    Context = {
        'forms':forms
    }
    return render (request,'website/contact.html',Context)

def project(request):
    image = Project1.objects.all()

    context = {
        'image' : image
    }
    return render (request,'website/project.html',context)


def Gallery (request):
    image = Images.objects.all()

    context = {
        'image' : image
    }
    return render (request,'website/gallery.html',context)

def Resume (request):
    return render (request,'website/Resume.html')
