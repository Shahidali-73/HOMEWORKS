from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

# Form page
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_customers')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

# Show all customers (sorted by name)
def all_customers(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'all_customers.html', {'customers': customers})

# Show customers with email ending in @example.com
def filtered_customers(request):
    customers = Customer.objects.filter(email__iendswith='@example.com').order_by('name')
    return render(request, 'filtered_customers.html', {'customers': customers})
