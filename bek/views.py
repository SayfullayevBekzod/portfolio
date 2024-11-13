from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .form import ContactForm
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')
def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')