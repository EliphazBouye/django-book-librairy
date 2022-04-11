from django import forms
from .models import Book

#Book form
class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = "__all__"
