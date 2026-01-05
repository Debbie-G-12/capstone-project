from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer
from books.models import Book
from django.utils import timezone

# --- API Views ---
class BorrowBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        if not book.is_available:
            return Response({'error': 'Book not available'}, status=400)
        book.is_available = False
        book.save()
        record = BorrowRecord.objects.create(user=request.user, book=book)
        serializer = BorrowRecordSerializer(record)
        return Response(serializer.data)

class ReturnBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, book_id):
        record = BorrowRecord.objects.filter(user=request.user, book_id=book_id, returned_at__isnull=True).first()
        if not record:
            return Response({'error': 'No active borrow found'}, status=400)
        record.returned_at = timezone.now()
        record.book.is_available = True
        record.book.save()
        record.save()
        serializer = BorrowRecordSerializer(record)
        return Response(serializer.data)

class BorrowHistoryView(generics.ListAPIView):
    serializer_class = BorrowRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return BorrowRecord.objects.filter(user=self.request.user)

# --- HTML Demo Views ---
def home(request):
    return render(request, 'borrowing/home.html')

def books_view(request):
    return render(request, 'borrowing/books.html')

def authors_view(request):
    return render(request, 'borrowing/authors.html')

def categories_view(request):
    return render(request, 'borrowing/categories.html')
