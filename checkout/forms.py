from django import forms
from .models import Order
from django.core.exceptions import ValidationError

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


        # To prevent form being submitted with non-numerical phonenumber  
        self.fields['phone_number'].widget.attrs[
            'pattern'] = "[0-9]{1,15}"

        # To prevent form being submitted with whitespace 
        # Credit https://github.com/AmyOShea/MS4-ARTstop/blob/main/checkout/forms.py   
        self.fields['full_name'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['street_address1'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['street_address2'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['town_or_city'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['county'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})
        self.fields['postcode'].widget.attrs.update(
            {'pattern': '.*\\S+.*'})

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gold'


