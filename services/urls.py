from django.urls import path
from . import views

urlpatterns = [
    path('', views.Services.as_view(), name='services'),
    path('add/', views.AddService.as_view(), name='add_service'),
    path(
        'edit/<int:pk>/', views.EditService.as_view(),
        name='edit_service'
        ),
    path(
        'delete/<int:pk>/', views.DeleteService.as_view(),
        name='delete_service'
        ),
]
