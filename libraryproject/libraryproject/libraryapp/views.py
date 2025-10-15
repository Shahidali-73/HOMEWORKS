from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

# Add new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# View all saved books
def view_books(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'view_books.html', {'books': books})
