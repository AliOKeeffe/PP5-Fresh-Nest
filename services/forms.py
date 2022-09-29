from django import forms
from .models import Service, Testimonial, PreviousProject
from products.widgets import CustomClearableFileInput

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gold'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = [
            'body',
            'service',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gold'


class AddProjectImageForm(forms.ModelForm):
    class Meta:
        model = PreviousProject
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-gold'
