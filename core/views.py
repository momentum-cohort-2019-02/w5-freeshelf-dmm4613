from django.shortcuts import render
from core.models import Book, Author, Category
from django.views import generic

class CategoriesListView(generic.ListView):
    model = Category

class CategoriesDetailView(generic.DetailView):
    model = Category
    
def index(request):
    """View function for home page of site."""

    book_list = Book.objects.all()[:3]
    category_list = Category.objects.all()[:5]

    context = {
        'book_list': book_list,
        'category_list': category_list,
    }

    # Render the HTML template index.html with the date in the context variable
    return render(request, 'index.html', context=context)
