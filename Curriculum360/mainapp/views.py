from django.shortcuts import render, redirect
from . import models


# Create your views here.

def  index(request):
    return render(request , 'index.html')



def home(request):
    return render(request,  'home.html')

def dashbord(request):
    return render(request, 'dashbord.html')