from django.db import models

class Author(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="authors/", blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def number_of_books(self):
        return self.book_set.count()

    def __str__(self):
        return self.name
