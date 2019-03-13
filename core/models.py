from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000)
    book_url = models.CharField(max_length=255)
    date_added = models.DateField(auto_now=True)
    category = models.ManyToManyField('Category')

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
    
    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slut(self):
        # If the slug is already set, stop here.
        if self.slug:
            return
        
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

class Category(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slut(self):
        # If the slug is already set, stop here.
        if self.slug:
            return
        
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Category.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        
        self.slug = slug

class Author(models.Model):

    name = models.CharField(max_length=255)  

    def __str__(self):
        return self.name