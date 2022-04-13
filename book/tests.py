from django.test import RequestFactory, TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import get_object_or_404
from django.http import HttpRequest

from .models import Book
from .views import upload, update_book
from .forms import BookForm


# def upload_book(book_name, author, email, describe):
    
#     return self.factory.post('upload_book', {'name': name, 'picture': image, 'author': author, 'email': email, 'describe': describe})
class BookModelTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        
        with open('test_data/test_img.png', 'rb') as img:
            picture = SimpleUploadedFile('test_img.png', b"img")
    
        self.upload = Book.objects.create(name='Test book',  picture=picture, author='sopho', email="sophonie@gmail.com", describe='simple book')
    
        self.url = reverse('update_book', args=[self.upload.id])
        
       
    
    def test_upload_book_form_view(self):
        #create a instance of a GET request
        request = self.factory.get('/upload_form')
        
        #test upload() view as if it were deployet at /upload_form
        response = upload(request)
        self.assertEqual(response.status_code, 200)
        
    def test_upload_book_and_redirect(self):
            img = SimpleUploadedFile(name='test_img.png', content=open('test_data/test_img.png', 'rb').read(), content_type='image/png')
            request = self.factory.post('upload_form', {'name': 'Test Book', 'picture': img, 'author': 'tester', 'email': 'goodemail@gmail.com', 'describe': 'simpe describe'})
            response = upload(request)
            response.client = Client()
            self.assertRedirects(response, reverse('home'), status_code = 302, target_status_code=200, fetch_redirect_response=True)

            
    def test_update_form_book(self):
           
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Test book')
            self.assertEqual(self.upload.author, 'sopho')
            
            #change
            
            request = HttpRequest()
            request.POST = {
                "name": "Name updated",
                "email": self.upload.email,
                "author": self.upload.author,
                "describe": self.upload.describe,
            }

            form = BookForm(request.POST,instance=self.upload)
            self.assertTrue(form.is_valid())
            form.save()
            self.upload.refresh_from_db()
            self.assertEqual(self.upload.name, 'Name updated')
           