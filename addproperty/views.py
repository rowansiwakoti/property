from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from listings.choices import BEDROOMS, PROPERTY_TYPES, PURPOSES, FURNISH_TYPE, FLOORS, DIRECTIONS, MIN_RENTAL_DURATION, ROAD_CONDITION, PARKING, UNIT_TYPES
from listings.models import Listing
from .forms import AddPropertyForm


# Create your views here.
def add_property(request):
    context = {
        'bedrooms': BEDROOMS,
        'property_types': PROPERTY_TYPES,
        'purposes': PURPOSES,
        'furnish_types': FURNISH_TYPE,
        'floors': FLOORS,
        'directions': DIRECTIONS,
        'min_rental_duration': MIN_RENTAL_DURATION,
        'road_condition': ROAD_CONDITION,
        'parking': PARKING,
        'unit': UNIT_TYPES
    }
    if request.method =='POST':
        form = AddPropertyForm(request.POST, request.FILES)
        print('hahahahah ', form.is_valid())
        print(form.errors)
        if form.is_valid():
             title = form.cleaned_data['title']
             property_type = form.cleaned_data['property_type']
             purpose = form.cleaned_data['purpose']
             price = form.cleaned_data['price']
             bedrooms = form.cleaned_data['bedrooms']
             bathrooms = form.cleaned_data['bathrooms']
             area = form.cleaned_data['area']
             city = form.cleaned_data['city']
             address = form.cleaned_data['address']
             photo_main = form.cleaned_data['photo_main']
             photo_1 = form.cleaned_data['photo_1']
             photo_2 = form.cleaned_data['photo_2']
             photo_3 = form.cleaned_data['photo_3']
             photo_4 = form.cleaned_data['photo_4']
             photo_5 = form.cleaned_data['photo_5']
             description = form.cleaned_data['description']

             formdata = Listing(
                title = title,
                property_type = property_type,
                purpose = purpose,
                price = price,
                bedrooms = bedrooms,
                bathrooms = bathrooms,
                area = area,
                city = city,
                address = address,
                photo_main = photo_main,
                photo_1 = photo_1,
                photo_2 = photo_2,
                photo_3 = photo_3,
                photo_4 = photo_4,
                photo_5 = photo_5,
                description = description,
                realtor_id = 1
             )
             formdata.save()
             context['form'] = AddPropertyForm()
             return render(request,'addproperty/add_property.html', context)
        else:
            context['error_message']= 'Property posting has failed. Try again.'
            context['form'] = AddPropertyForm()
            return render(request, 'addproperty/add_property.html', context)
    
    else:
        context['form'] = AddPropertyForm()

    return render(request,'addproperty/add_property.html', context)
