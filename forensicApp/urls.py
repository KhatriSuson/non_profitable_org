from django.urls import path
from forensicApp import views


urlpatterns = [
    path('', views.home, name="home" ),
    path('about/', views.about, name='about'),
    path('about/<int:pk>/', views.about_detail, name='about_detail'),
    path('service/', views.services_view, name='service'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name="contact"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank_you/', views.thank_you, name='thank_you'),
]