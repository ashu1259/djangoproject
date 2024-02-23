from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'djangoapp/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        Book.objects.create(title=title, author=author, publication_date=publication_date)
        return redirect('book_list')
    return render(request, 'djangoapp/book_form.html')

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        book.title = title
        book.author = author
        book.publication_date = publication_date
        book.save()
        return redirect('book_list')
    return render(request, 'djangoapp/book_form.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'djangoapp/book_confirm_delete.html', {'book': book})
