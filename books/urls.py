from django.urls import path
from books.views import add_book, book_list

urlpatterns = [
    path("add/", add_book, name="add_book"),
    path("list/", book_list, name="book_list"),
]
