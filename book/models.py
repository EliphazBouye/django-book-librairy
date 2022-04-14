from django.db import models

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30, default="anonymous")
    email = models.EmailField(blank = True)
    describe = models.TextField(default = "Django CRUD Tutorial")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name