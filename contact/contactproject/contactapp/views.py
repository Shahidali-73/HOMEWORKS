from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return render(request, 'thank_you.html', {'name': contact.full_name})
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})
