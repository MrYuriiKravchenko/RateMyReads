from rest_framework import viewsets
from .serializers import BookSerializer, GenreSerializer, CommentSerializer
from .models import Book, Genre, Comment
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework import filters
from rest_framework import generics

class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 8
    page_query_param = 'page_size'
    ordering = 'title'

class BookViewSet(viewsets.ModelViewSet):
    search_fields = ['title', 'author']
    filter_backends = (filters.SearchFilter,)
    serializer_class = BookSerializer
    lookup_field = 'slug'
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny] 
    pagination_class = PageNumberSetPagination

class GenreReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [permissions.AllowAny]

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        book_slug = self.kwargs['book_slug'].lower()
        book = Book.objects.get(slug=book_slug)
        return Comment.objects.filter(book=book)