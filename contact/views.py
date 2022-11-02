from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.views import generic, View
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact


class ContactUs(View):
    """
    This view is used to display the contact form and
    handle GET and POST requests
    """

    def get(self, request):
        """
        Renders the contact form
        """
        if request.user.is_authenticated:
            form = ContactForm(initial={'email': request.user.email})
        else:
            form = ContactForm()

        return render(
            request,
            "contact/contact.html",
            {
                "contact_form": form,
            },
        )

    def post(self, request):
        """
        This method is called when a POST request is made to the view
        via the contact form
        """
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            cust_name = contact_form.instance.name
            cust_email = contact_form.instance.email
            subject = contact_form.instance.enquiry_type
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'subject': subject})
            message = contact_form.instance.message
            message = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'cust_name': cust_name, 'message': message}
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )

            contact_form.save()
            messages.success(self.request, 'Your enquiry has been sent')

            target = "home/index.html"
            context = {"plain_message": True}

        else:
            messages.error(request, """Form failed. Please ensure the
            form is valid """)

            target = "contact/contact.html"
            context = {
                "plain_message": True,
                "contact_form": contact_form
                }

        return render(request, target, context)


class Enquiries(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """ This view is used to display all enquiries """
    model = Contact
    template_name = 'contact/enquiries_dashboard.html'

    def test_func(self):
        """
        ensures only superuser can view enquiries
        """
        if self.request.user.is_superuser:
            return True

    def get_context_data(self, **kwargs):
        """
        ensures success message doesn't include bag items
        """
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class EnquiryDetail(
        LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    """ This view is used to display selected enquiry detail """
    model = Contact
    template_name = 'contact/enquiry_detail.html'

    def test_func(self):
        """
        ensures only superuser can add view enquiries
        """
        if self.request.user.is_superuser:
            return True


class DeleteEnquiry(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow the superuser to delete an enquiry
    """
    model = Contact
    template_name = 'contact/delete_enquiry.html'
    success_message = "Enquiry deleted successfully"
    success_url = reverse_lazy('enquiries')

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
        return super(DeleteEnquiry, self).delete(request, *args, **kwargs)
