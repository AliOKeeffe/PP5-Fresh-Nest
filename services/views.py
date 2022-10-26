"""Service Views"""

from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Service, Testimonial, PreviousProject
from django.urls import reverse_lazy
from .forms import ServiceForm, TestimonialForm, AddProjectImageForm


class Services(generic.ListView):
    """ This view is used to display all services """
    model = Service
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddService(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.CreateView):

    """This view is used to allow site owner to add a new service"""
    form_class = ServiceForm
    template_name = 'services/add_service.html'
    success_message = "%(calculated_field)s was created successfully"

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
    This view is used to allow the superuser to delete a service
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
    template_name = 'services/testimonials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddTestimonial(
        LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):

    """This view is used to allow a user to add a testimonial"""
    form_class = TestimonialForm
    template_name = 'services/add_testimonial.html'
    success_message = "Your testimonial was added successfully"

    def form_valid(self, form):
        """
        Override the form_valid() method in model form view
        in order to set the signed in user as the name on the testimonial.
        """
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditTestimonial(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView):

    """
    This view is used to allow logged in users to edit their own testimonials
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'services/edit_testimonial.html'
    success_message = "Testminonial edited successfully"

    def test_func(self):
        """
        Prevent another user from editing user's testminonial
        """
        testimonial = self.get_object()
        return testimonial.name == self.request.user\
            or self.request.user.is_superuser


class DeleteTestimonial(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own testimonials
    """
    model = Testimonial
    template_name = 'services/delete_testimonial.html'
    success_message = "Testminonial successfully deleted"
    success_url = reverse_lazy('testimonials')

    def test_func(self):
        """
        Prevent another user from deleting another user's testminonial
        """
        testimonial = self.get_object()
        return testimonial.name == self.request.user\
            or self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.
        Credit: https://stackoverflow.com/questions/24822509/
        success-message-in-deleteview-not-shown
        """
        messages.success(self.request, self.success_message)
        return super(DeleteTestimonial, self).delete(request, *args, **kwargs)


class ProjectGallery(generic.ListView):
    """ This view is used to display photo gallery of previous projects """
    model = PreviousProject
    template_name = 'services/project_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddProjectImage(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.CreateView):
    """
    This view is used to allow the site owner to add
    images of previous projects to the gallery
    """
    form_class = AddProjectImageForm
    template_name = 'services/add_project_image.html'
    success_message = "Your image was added successfully"

    def test_func(self):
        """
       Ensure only superuser can add an image
        """
        if self.request.user.is_superuser:
            return True


class DeleteProjectImage(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow the superuser to delete images from the gallery
    """
    model = PreviousProject
    template_name = 'services/delete_project_image.html'
    success_message = "Image successfully deleted"
    success_url = reverse_lazy('project_gallery')

    def test_func(self):
        """
       Ensure only superuser can delete an image
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
        return super(DeleteProjectImage, self).delete(request, *args, **kwargs)
