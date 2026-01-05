from django.contrib import admin
from django.urls import path, include
from borrowing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Landing page
    path('', views.home, name='home'),
    
    # Pages for demo
    path('books/', views.books_view, name='books'),
    path('authors/', views.authors_view, name='authors'),
    path('categories/', views.categories_view, name='categories'),
    path('borrow/history/', views.borrow_history_view, name='borrow_history'),
    
    # API endpoints
    path('api/accounts/', include('accounts.urls')),
    path('api/books/', include('books.urls')),
    path('api/authors/', include('books.urls')),  # adapt if needed
    path('api/categories/', include('books.urls')),  # adapt if needed
    path('api/borrowing/', include('borrowing.urls')),
]
