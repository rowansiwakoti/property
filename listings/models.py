from django.db import models
from datetime import datetime
from realtors.models import Realtor
from .choices import PURPOSES, PROPERTY_TYPES, BEDROOMS, FURNISH_TYPE, ROAD_CONDITION, MIN_RENTAL_DURATION, DIRECTIONS, PROVINCE

class Province(models.Model):
  name = models.CharField(max_length=21)

  def __str__(self):
    return self.name


class District(models.Model):
  province = models.ForeignKey(Province, on_delete=models.CASCADE)
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name


# Create your models here.
class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) #Realtor is another model
  title = models.CharField(max_length=100)
  property_type = models.CharField(max_length=17, choices=PROPERTY_TYPES)
  purpose = models.CharField(max_length=4, choices=PURPOSES)

  price = models.IntegerField()
  furnish_type = models.CharField(max_length=15, choices=FURNISH_TYPE, default='Furnished')
  area = models.CharField(max_length=50, blank=True)
  bedrooms = models.IntegerField(choices=BEDROOMS)
  bathrooms = models.IntegerField(choices=BEDROOMS)
  living = models.IntegerField(choices=BEDROOMS, default=0)
  kitchen = models.IntegerField(choices=BEDROOMS, default=0)
  floor = models.IntegerField(default=1)
  # parking missing
  road_size = models.IntegerField(default=20)
  road_condition = models.CharField(max_length=20, choices=ROAD_CONDITION, default='Kachchi')
  facing_direction = models.CharField(choices=DIRECTIONS, max_length=40, default='East')
  # min_rental_duration = models.CharField(max_length=11, choices=MIN_RENTAL_DURATION, default='1 Year')
  available_from = models.DateTimeField(blank=True, default=datetime.now)
  built_year = models.DateTimeField(blank=True, default=datetime.now)

  province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)
  district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
  city = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  description = models.TextField(max_length=500, blank=True)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

 
  def __str__(self): #In the Django Admin, there will be a table that displays each listing and we need to pick the main field
                     #that needs to be display, so we choose 'title' 
    return self.title





    # image size reducers link
    # https://medium.com/@eyakubsorkar/how-to-compress-image-while-uploading-to-the-directory-django-bdd3fcab0b23
    # https://pythoncircle.com/post/707/how-to-compress-the-uploaded-image-before-storing-it-in-django/
    # https://stackoverflow.com/questions/52183975/how-to-compress-the-image-before-uploading-to-s3-in-django