from django.shortcuts import render, get_object_or_404
from core.models import Book, Author, Category
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

class CategoriesListView(generic.ListView):
    model = Category

class CategoriesDetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(CategoriesDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['category_list'] = Category.objects.all()
        return context


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

@require_http_methods(['POST'])
@login_required
def book_favorite_view(request, book_pk):
    dog = get_object_or_404(Book, pk=book_pk)

    favorite, created = request.user.favorite_set.get_or_create(book=book)

    if created:
        messages.success(request, f"You have favorited {book.name}.")
    else:
        messages.info(request, f"You have unfavorited {book.name}.")
        favorite.delete()

    return redirect(book.get_absolute_url)