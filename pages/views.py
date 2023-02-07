from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import BEDROOMS

# Create your views here.

def index(request):
    sell_list = Listing.objects.order_by('-list_date').filter(is_published=True, purpose='sell')[:6] # [:6] means only showing 6 listings
    rent_list = Listing.objects.order_by('-list_date').filter(is_published=True, purpose='rent')[:6]
    context = {
        'sell_list': sell_list,
        'rent_list': rent_list,
        'bedroom_choices': BEDROOMS,
    }
    return render(request,'pages/index.html', context)


def about(request):

    # Get all realtors
    realtorsAll = Realtor.objects.order_by('-hire_date')

    # Get mvp
    mvpRealtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtorsAll,
        'mvpRealtors': mvpRealtors,
    }
    return render(request,'pages/about.html',context)
