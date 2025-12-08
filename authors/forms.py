from django import forms
from authors.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "email", "bio", "profile_image"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }
