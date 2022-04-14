from django.contrib import admin
from .models import Book, Category

#Book
admin.site.register(Book)
admin.site.register(Category)
