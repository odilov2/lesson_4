from django.shortcuts import render
from .models import Book


def landing_view(request):
    return render(request, 'library/landing_page.html')


def book_view(request):
    books = Book.objects.all()

    return render(request, 'library/books_list.html', {'books': books})