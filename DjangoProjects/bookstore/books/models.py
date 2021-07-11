from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Author(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')


class Book(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    created = models.DateTimeField('date created')
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # on_delete: kitabın yazarı silinirse, kitapları da silinir
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True)
