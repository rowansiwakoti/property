from django import forms
from listings.models import Listing
from listings.choices import PURPOSES, PROPERTY_TYPES


class AddPropertyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
        # add form-control to a specific field
        # self.fields['photo_main'].widget.attrs['class']='form-control'

        # self.fields['district'].queryset = District.objects.none()

    class Meta:
        model = Listing
        # fields = '__all__'
        fields = ['title', 'property_type', 'purpose', 'price', 'bedrooms', 'bathrooms', 'area',
                  'city', 'address', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'description', 'furnish_type']
        # labels = {'property_type': 'Property Type', 'sqft': 'Area (Sqft.)', 'photo_main': 'Photo Main'}
        widgets = {
             'title': forms.TextInput(attrs= {'placeholder': 'For eg: Well Furnished 3BHK apartment'}),
             'price': forms.NumberInput(attrs= {'placeholder': 'Enter price'}),
             'area': forms.TextInput(attrs= {'placeholder': 'For eg: 7 aana 2 paisa'}),
             'city': forms.TextInput(attrs= {'placeholder': 'Enter city name'}),
             'address': forms.TextInput(attrs= {'placeholder': 'Enter address'}),
             'description': forms.Textarea(attrs= {'placeholder': 'Enter description and/or any other details about the property', 'rows': 7}),
            }
        # help_texts = {}
        # error_messages = {
        #     'title': {
        #         'required': 'This field is required'
        #     },
        #     'purpose': {
        #         'required': 'This field is required'
        #     }
        # }