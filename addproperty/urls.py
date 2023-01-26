from django.urls import path

from . import views

urlpatterns = [
    path('addproperty/', views.add_property, name='addproperty')
]