from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('books/', ListBooks.as_view(), name='list_books'),
    path('books/<int:id>', DetailBook.as_view(), name='detail_book'),
    path('user_area/', user_area, name='user_area'),
    path('books/create/', create_books, name='create_books'),
    path('login/', login_profile, name='login'),
    path('logout/', logout_profile, name='logout'),
]