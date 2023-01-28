from django.db import models
from datetime import datetime
from realtors.models import Realtor
from .choices import PURPOSES, PROPERTY_TYPES


# Create your models here.
class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) #Realtor is another model
  title = models.CharField(max_length=200)
  purpose = models.CharField(max_length=4, choices=PURPOSES, default='sell')
  property_type = models.CharField(max_length=17, choices=PROPERTY_TYPES, default='apartments')
  address = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  sqft = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self): #In the Django Admin, there will be a table that displays each listing and we need to pick the main field
                     #that needs to be display, so we choose 'title' 
    return self.title





    # image size reducers link
    # https://medium.com/@eyakubsorkar/how-to-compress-image-while-uploading-to-the-directory-django-bdd3fcab0b23
    # https://pythoncircle.com/post/707/how-to-compress-the-uploaded-image-before-storing-it-in-django/
    # https://stackoverflow.com/questions/52183975/how-to-compress-the-image-before-uploading-to-s3-in-django