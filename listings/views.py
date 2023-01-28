from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import BEDROOMS, PROPERTY_TYPES, PURPOSES


# Create your views here.
def index(request):

    listingsAll = Listing.objects.order_by('-list_date').filter(is_published=True) #Most recent listings should be first and only those published will be shown

    paginator = Paginator(listingsAll, 50)

    page = request.GET.get('page') #'page' is the URL parameter that we are looking for
    paged_listingsAll = paginator.get_page(page)

    context = {
        'listings': paged_listingsAll
    }

    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk=listing_id)  # If it doesn't exist it will return 404
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # purpose in the search form
    if 'purpose' in request.GET:
        purpose = request.GET['purpose'] #'purpose' is the form field
        if purpose:
            queryset_list = queryset_list.filter(purpose__iexact=purpose)

    # Property Types
    if 'property_type' in request.GET:
        property_type = request.GET['property_type']
        if property_type:
            queryset_list = queryset_list.filter(property_type__iexact=property_type)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    # Min Price
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        if min_price:
            queryset_list = queryset_list.filter(price__gte=min_price) # 'gte' can be used for "greater than or equal to"

    # Max Price
    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        if max_price:
            queryset_list = queryset_list.filter(price__lte=max_price) # 'lte' can be used for "less than or equal to"


    context = {
        'bedrooms': BEDROOMS,
        'purposes': PURPOSES,
        'property_types': PROPERTY_TYPES,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html',context)