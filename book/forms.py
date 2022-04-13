from django.forms import ModelForm
from .models import Book

#Book form
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", "picture", "author", "email", "describe"]
