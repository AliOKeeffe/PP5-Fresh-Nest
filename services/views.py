"""Service Views"""

from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, Testimonial, PreviousProject
from django.urls import reverse_lazy
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


class EditService(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView
        ):
    """
    This view is used to allow the superuser to edit Service details
    """
    model = Service
    form_class = ServiceForm
    template_name = 'services/edit_service.html'
    success_message = "%(calculated_field)s was edited successfully"

    def form_valid(self, form):
        """
        This method is called when valid form data has been posted.
        """
        return super().form_valid(form)

    def test_func(self):
        """
        Ensure only superuser can edit service details
        """
        if self.request.user.is_superuser:
            return True

    def get_success_message(self, cleaned_data):
        """
        Override the get_success_message() method to add the service type
        into the success message.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.type,
        )


class DeleteService(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own recipes
    """
    model = Service
    template_name = 'services/delete_service.html'
    success_message = "Service deleted successfully"
    success_url = reverse_lazy('services')

    def test_func(self):
        """
       Ensure only superuser can edit service details
        """
        if self.request.user.is_superuser:
            return True

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteService, self).delete(request, *args, **kwargs)


class Testimonials(generic.ListView):
    """ This view is used to display all testimonials """
    model = Testimonial
    template_name = 'services/testimonial.html'
