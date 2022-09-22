from django.urls import path
from . import views

urlpatterns = [
    path('', views.Services.as_view(), name='services'),
    path('add/', views.AddService.as_view(), name='add_service'),
]
