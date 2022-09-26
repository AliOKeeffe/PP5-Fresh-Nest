from django.shortcuts import render
from django.core.mail import send_mail
from django.views import generic, View
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
from .models import Contact

# Create your views here.

# class ViewEnquiries(generic.ListView):
#     """ This view is used to display contact form """
#     model = Contact
#     template_name = 'contact/contact.html'


class ContactUs(View):
    """
    This view is used to display the contact form and
    handle GET and POST requests
    """

    def get(self, request):
        """
        Renders the contact form
        """
        return render(
            request,
            "contact/contact.html",
            {
                "contact_form": ContactForm(),
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
            # Sends confimation email to customer
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [cust_email]
            )

            contact_form.save()

        return render(
            request,
            "contact/contact.html",
            {
                "contact_form": ContactForm(),
            },
        )
