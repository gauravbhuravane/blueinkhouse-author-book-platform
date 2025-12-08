from django import forms
from books.models import Book
from authors.models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "description", "genre", "cover_image", "author"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # only approved authors can be selected
        self.fields["author"].queryset = Author.objects.filter(status="approved")
