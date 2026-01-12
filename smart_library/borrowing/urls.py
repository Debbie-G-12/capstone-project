from django.urls import path
from .views import BorrowBookView, ReturnBookView, BorrowHistoryView
from . import views

urlpatterns = [
    # API actions
    path('borrow/<int:book_id>/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='return-book'),
    path('borrow/history/', BorrowHistoryView.as_view(), name='borrow-history'),

    # UI pages
    path('', views.home, name='home'),
    path('books/', views.books_view, name='books'),          # <-- 
    path('authors/', views.authors_view, name='authors'),    # <-- 
    path('categories/', views.categories_view, name='categories'),  # <-- 
]
