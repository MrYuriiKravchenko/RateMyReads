from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, GenreViewSet, CommentView, RatingViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('genre', GenreViewSet, basename='genre')
router.register('ratings', RatingViewSet, basename='ratings')


urlpatterns = [
    path('', include(router.urls)),
    path('comments/', CommentView.as_view()),
    path('comments/<slug:book_slug>/', CommentView.as_view()),
    path('books/<slug:book_pk>/ratings/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='book-ratings')
]

