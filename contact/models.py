""" Contact Models """

from django.db import models
from services.models import Service
from django.urls import reverse

# Create your models here.


class Contact(models.Model):
    """ Model for Contact """
    name = models.CharField(max_length=122, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    enquiry_type = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='contact')
    message = models.TextField(max_length=500, default='')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Get url after user submits enquiry """
        return reverse('home')

    class Meta:
        """ To display the equiries by date in ascending order """
        ordering = ['-date']

    def __str__(self):
        return f"Enquiry: {self.enquiry_type} from {self.name}"
