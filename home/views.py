"""Home Views"""

from django.views import generic


class Home(generic.TemplateView):
    """This view is used to display the home page"""
    template_name = "home/index.html"
