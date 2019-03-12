from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Category(models.Model):
    """Model representing a book category."""
    name = models.CharField(max_length=200, help_text='Enter a book category (e.g. Javascript)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    url = models.CharField(max_length=255, null=True)
    # slug = models.CharField(max_length=100)
    date_added = models.DateField(max_length=25, auto_now=False)
    
    # ManyToManyField used because category can contain many books. Books can ocver many categories.
    #Category class has already been defined so we can specify the object above.
    category = models.ManyToManyField(Category, related_name='categories', help_text='Select a category for this book')

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('index')

class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.name