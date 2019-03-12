from django.contrib import admin
from core.models import Author, Category, Book

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
