"""Services Models"""

from django.db import models
from django.urls import reverse


class Service(models.Model):
    """ Model for Service """
    type = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        """Get url after superuser adds/edits service"""
        return reverse('services')


class Testimonial(models.Model):
    """Model for Testimonial"""
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='testimonial')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """ To display the testimonials by created_on in ascending order """
        ordering = ['created_on']

    def get_absolute_url(self):
        """Get url after user adds/edits testimonial"""
        return reverse('testimonials')

    def __str__(self):
        return f"Testimonial {self.body} by {self.name}"


class PreviousProject(models.Model):
    """Model for previous projects"""
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='previous_project')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=254)

    def get_absolute_url(self):
        """Get url after user adds project image"""
        return reverse('project_gallery')

    def __str__(self):
        return f"Project: {self.service} in {self.location}"
