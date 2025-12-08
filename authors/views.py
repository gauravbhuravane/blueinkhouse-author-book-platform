from django.shortcuts import render, redirect, get_object_or_404
from authors.models import Author
from authors.forms import AuthorForm

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # status will be pending by default
            return redirect("author_list")
    else:
        form = AuthorForm()
    return render(request, "authors/add_author.html", {"form": form})


def author_list(request):
    authors = Author.objects.all().order_by("-created_at")
    return render(request, "authors/author_list.html", {"authors": authors})


def approve_author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.status = "approved"
    author.save()
    return redirect("author_list")
