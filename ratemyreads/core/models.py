from django.db import models
from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        indexes= [
            models.Index(fields=['name']),
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    author = models.CharField(max_length=200)
    images_book = models.ImageField(upload_to='books/%Y/%m/%d', null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='genre_books')
    pub_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=700)
    slug = models.SlugField()

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
        ]
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['book']),
            models.Index(fields=['user']),
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'{self.user} - {self.book} - {self.text[:20]}'
    
class Rating(models.Model):
    book = models.ForeignKey(Book, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_ratings', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['book']),
            models.Index(fields=['user']),
            models.Index(fields=['score']),
        ]
    
    def __str__(self):
        return f'{self.user} - {self.book} - {self.score}'
    