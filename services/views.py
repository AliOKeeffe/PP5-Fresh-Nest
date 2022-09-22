"""Service Views"""

from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, Testimonial, PreviousProject
from .forms import ServiceForm


class Services(generic.ListView):
    """ This view is used to display all services """
    model = Service
    template_name = 'services/services.html'


class AddService(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.CreateView):

    """This view is used to allow site owner to add a new service"""
    form_class = ServiceForm
    template_name = 'services/add_service.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function overrides the get_success_message() method to add
        the service type into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.type,
        )

    def test_func(self):
        """
        ensures only superuser can add new serivces
        """
        if self.request.user.is_superuser:
            return True
