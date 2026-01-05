from django.urls import path
from . import views
from .views import BorrowBookView, ReturnBookView, BorrowHistoryView

urlpatterns = [
    # API endpoints for borrowing
    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='return-book'),
    path('history/', BorrowHistoryView.as_view(), name='borrow-history'),  # Optional, leave if you want API only
    
    # Demo HTML pages
    path('', views.home, name='home'),  # Home page
    path('books/', views.books_view, name='books'),
    path('authors/', views.authors_view, name='authors'),
    path('categories/', views.categories_view, name='categories'),
]
