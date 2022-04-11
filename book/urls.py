from distutils.debug import DEBUG
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('upload-book', views.upload, name="upload_book"),
    path('update/<int:book_id>', views.update_book, name="update_book"),
    path('delete/<int:book_id>', views.delete_book, name="delete_book"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


#if DEBUG:
# urlpatterns += 
# urlpatterns += 