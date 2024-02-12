from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog1-home'),
    path('about/', views.about, name='blog1-about'),
]
