from django.urls import path
from authors.views import add_author, author_list, approve_author_view

urlpatterns = [
    path("add/", add_author, name="add_author"),
    path("list/", author_list, name="author_list"),
    path("<int:pk>/approve/", approve_author_view, name="approve_author"),
]
