from django.shortcuts import render, redirect
from django.db.models import Q
from books.models import Book
from books.forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})


def book_list(request):
    query = request.GET.get("q", "")
    books = Book.objects.all().select_related("author")

    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(genre__icontains=query)
            | Q(author__name__icontains=query)
        )

    context = {
        "books": books,
        "query": query,
    }
    return render(request, "books/book_list.html", context)
