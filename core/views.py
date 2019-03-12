from django.shortcuts import render
from core.models import Book, Author, Category
from django.views import generic
    
class BookListView(generic.ListView):
    model = Book

def index(request):
    """View function for home page of site."""

    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the date in the context variable
    return render(request, 'index.html', context=context)
