from django.contrib import admin
from core.models import Genre, Book, Comment, Rating



class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'text', 'created']
    list_filter = ['created', 'user']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'score']
    list_filter = ['score', 'user']


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class RatingInLine(admin.TabularInline):
    model = Rating
    extra = 0

class GenreInline(admin.StackedInline):  
    model = Book.genre.through
    extra = 1 # Количество пустых форм для добавления новых объектов


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('genre',)  # Исключить поле authors, так как мы будем работать через инлайн
    list_display = [
        'title', 'isbn', 'author', 'pub_date', 'slug'
        ]
    inlines = [CommentInLine, RatingInLine, GenreInline]

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    inlines = [GenreInline]



admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)

