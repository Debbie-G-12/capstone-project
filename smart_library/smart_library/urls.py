from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),
    path('api/books/', include('books.urls')),
    path('api/authors/', include('authors.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/borrowing/', include('borrowing.urls')),
]
