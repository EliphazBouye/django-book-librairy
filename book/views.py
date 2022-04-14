import os
from django.shortcuts import redirect, render , get_object_or_404, get_list_or_404
from .models import Book
from .forms import BookForm
from django.http import HttpResponse

#Book home list all book
def home(request):
    books = Book.objects.all()
    return render(request, 'book/librairy.html', {'books': books})

# add new book and upload image of the book
def upload(request):
    
    #check the http method
    if request.method == 'POST':
        # get post fields and file field submited
        upload = BookForm(request.POST, request.FILES)
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
        upload = BookForm()
        return render(request, 'book/upload_form.html', {'upload' : upload})

#update a book
def update_book(request, book_id):
    book_id = int(book_id)
    #get a book from id
    
    if request.method == 'POST':
        book_sel =  get_object_or_404(Book,pk=book_id) 
        book_form = BookForm(data=request.POST,files=request.FILES,instance= book_sel)
        #check if book form is valid
        if book_form.is_valid():
            print("Valid Update form")
            #get image path
            # image_path = book_sel.picture.path
            # if os.path.exists(image_path):
            #     # remove old image if it exist
            #     os.remove(image_path)
            book_form.save()
            return redirect('home')
        else:
            print("Invalid update form")
            print(book_form)
            print(book_form.errors)
    else:
        book_sel =  get_object_or_404(Book,pk=book_id) 
        book_form = BookForm(instance= book_sel)
        
    return render(request, 'book/upload_form.html', {'upload': book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('home')
    book_sel.delete()
    return redirect('home')