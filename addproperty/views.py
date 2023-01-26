from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def add_property(request):
    return render(request,'addproperty/add_property.html')
