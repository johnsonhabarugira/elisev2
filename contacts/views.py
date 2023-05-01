from django.shortcuts import render, redirect,get_object_or_404
from .forms import ContactForm
from .models import Contact
from users.models import profile

def contact(request):
    company_cont = profile.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = ContactForm()
    #contact_res = profile.objects.get(id=pk)
    
    
        form = ContactForm()
    context = {'form': form, 'company_cont': company_cont}
    return render(request, 'contacts/contact.html', context)

