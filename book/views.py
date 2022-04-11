import os
from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm
from django.http import HttpResponse

#Book home list all book
def home(request):
    books = Book.objects.all()
    return render(request, 'book/librairy.html', {'books': books})

# add new book and upload image of the book
def upload(request):
    upload = BookForm()
    #check the http method
    if request.method == 'POST' or None:
        # get post fields and file field submited
        upload = BookForm(request.POST or None, request.FILES or None)
        # check if form is valid
        if upload.is_valid():
            print("Valid form")
            upload.save()
            return redirect('home')
        else:
            # if form is not valid information
           print("Invalid form")
           print(upload.errors)
           return render(request, 'book/upload_form.html', {'upload': upload})
           
    else:
        # if use want add book form 
        return render(request, 'book/upload_form.html', {'upload' : upload})

#update a book
def update_book(request, book_id):
    book_id = int(book_id)
    #get a book from id
    try: 
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_form = BookForm(request.POST or None, request.FILES or None, instance= book_sel)
    
    #check if book form is valid
    if book_form.is_valid():
        #get image path
        image_path = book_sel.picture.path
        if os.path.exists(image_path):
            # remove old image if it exist
            os.remove(image_path)
        book_form.save()
        
        return redirect('home')
    return render(request, 'book/upload_form.html', {'upload': book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_sel.delete()
    return redirect('home')