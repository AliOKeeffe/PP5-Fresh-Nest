from django import forms
from .models import Service, Testimonial, PreviousProject


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = [
            'body',
            'service',
        ]

class AddProjectImageForm(forms.ModelForm):
    class Meta:
        model = PreviousProject
        fields = '__all__'
