from django.shortcuts import render
from .models import Term

def terms(request):
    terms = Term.objects.all()
    return render(request, 'termsandconditions/terms.html', {'terms': terms})
