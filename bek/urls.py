from django.contrib import admin
from django.urls import path
from .views import *
# app_name = 'bek'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('resume/', resume, name='resume'),
    path('portfolio/', portfolio, name='portfolio'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),

]