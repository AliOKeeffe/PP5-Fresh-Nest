from django.urls import path
from . import views

urlpatterns = [
    path('', views.Services.as_view(), name='services'),
    path('testimonials/', views.Testimonials.as_view(), name='testimonials'),
    path('add/', views.AddService.as_view(), name='add_service'),
    path(
        'edit/<int:pk>/', views.EditService.as_view(),
        name='edit_service'
        ),
    path(
        'delete/<int:pk>/', views.DeleteService.as_view(),
        name='delete_service'
        ),
    path(
        'testimonials/add/', views.AddTestimonial.as_view(),
        name='add_testimonial'
        ),
    path(
        'testimonials/edit/<int:pk>/', views.EditTestimonial.as_view(),
        name='edit_testimonial'
        ),
    path(
        'testimonials/delete/<int:pk>/', views.DeleteTestimonial.as_view(),
        name='delete_testimonial'
        ),
]
