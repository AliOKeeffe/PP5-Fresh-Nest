from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUs.as_view(), name='contact'),
    path('enquiries/', views.Enquiries.as_view(), name='enquiries'),
    path(
        'enquiries/<int:pk>/',
        views.EnquiryDetail.as_view(), name='enquiry_detail'
        ),
    path(
        'enquiries/delete/<int:pk>/', views.DeleteEnquiry.as_view(),
        name='delete_enquiry'
        ),
]
