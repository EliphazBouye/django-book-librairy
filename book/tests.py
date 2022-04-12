from django.test import RequestFactory, TestCase, Client
from django.urls import reverse

from .models import Book
from .views import upload

# def upload_book(book_name, picture, author, email, describe):
#     # return Book.objects.create(name=book_name, picture=picture, author=author, email=email,describe=describe)
#     return self.factory.post('upload_book', {'name': name, 'picture': image, 'author': author, 'email': email, 'describe': describe})
class BookModelTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_upload_book_form_view(self):
        #create a instance of a GET request
        request = self.factory.get('/upload_form')
        
        #test upload() view as if it were deployet at /upload_form
        response = upload(request)
        self.assertEqual(response.status_code, 200)
        
    def test_upload_book_and_redirect(self):
        with open('test_data/test_img.png', 'rb') as img:
            request = self.factory.post('upload_book', {'name': 'Test Book', 'picture': img, 'author': 'tester', 'email': 'goodemail@gmail.com', 'describe': 'simpe describe'})
            response = upload(request)
            response.client = Client()
            self.assertRedirects(response, reverse('home'), status_code = 302, target_status_code=200, fetch_redirect_response=True)