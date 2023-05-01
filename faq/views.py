from django.shortcuts import render
from .models import FAQ

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq.html', {'faqs': faqs})
