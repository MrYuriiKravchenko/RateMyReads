from rest_framework import serializers
from .models import Book, Genre, Comment, Rating
from users.models import User


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre 
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)


    class Meta:
        model = Book 
        fields = ['id', 'description', 'title', 'isbn', 'author', 'pub_date', 'images_book', 'slug', 'genre']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="user", queryset=User.objects.all())
    book = serializers.SlugRelatedField(slug_field="slug", queryset=Book.objects.all())

    class Meta:
        model = Comment 
        fields = ['id', 'book', 'user', 'text', 'created']
        lookup_field = 'id'
        extra_kwargs = {
            'url': {'lookup_field': 'id'}
        }


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating 
        fields = ['id', 'score']
        read_only_fields = ['id']
