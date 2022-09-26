from django import forms
from .models import Service, Testimonial


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