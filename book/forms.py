from dataclasses import fields
from django import forms
from .models import Book, Category



class CustomMMF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, book) -> str:
        return "%s" % book.name 


#Book form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "picture", "author", "email", "describe"]
    


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
    
    name = forms.CharField()
    books = CustomMMF(
        queryset=Book.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )