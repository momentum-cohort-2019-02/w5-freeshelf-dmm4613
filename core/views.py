from django.shortcuts import render
from core.models import Book, Author, Category
from django.views import generic


def index(request):
    """View function for home page of site."""

    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    book_list = Book.objects.all()[:3]
    category_list = Category.objects.all()[:5]

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'book_list': book_list,
        'category_list': category_list,
    }

    # Render the HTML template index.html with the date in the context variable
    return render(request, 'index.html', context=context)
