from django.contrib import admin
from django.urls import path, include

from authors.views import author_list

# 👇 add these two imports
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", author_list, name="home"),
    path("admin/", admin.site.urls),
    path("authors/", include("authors.urls")),
    path("books/", include("books.urls")),
]

# 👇 add this at the bottom
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
