from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('customer/<int:pk>/', views.customData),
]
