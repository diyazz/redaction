from django.contrib import admin

# Register your models here.
from .models import Author, Book, Redaction


admin.site.register(Author)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):


    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name


    list_display = ('title','author')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'redaction')

@admin.register(Redaction)
class RedactionAdmin(admin.ModelAdmin):
    pass
