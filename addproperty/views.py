from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from listings.choices import BEDROOMS, PROPERTY_TYPES, PURPOSES

# Create your views here.
def add_property(request):
    context = {
        'bedrooms': BEDROOMS,
        'property_types': PROPERTY_TYPES,
        'purposes': PURPOSES
    }
    return render(request,'addproperty/add_property.html', context)
