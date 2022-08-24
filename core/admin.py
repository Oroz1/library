from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from core.models import *


class BookAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Book
        fields = '__all__'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'author', 'get_image')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'id')
    list_filter = ('author', 'tags', 'genre',)
    form = BookAdminForm
    def get_image(self, instance):
        return mark_safe(
            f'<img src="{instance.image.url}" alt="{instance.title}" width="150px" />'
        )
    get_image.short_description = 'Изображение'
    readonly_fields = ('get_image',)
    fields = (
        'title',
        'file',
        'genre',
        'tags',
        'image',
        'description',
        'author',
        'get_image',        
    )
    


@admin.register(Tag)
class TagaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):   
    list_display = ('title',)
    

class AuthorAdminForm(forms.ModelForm):
    information = forms.CharField(label='Биография', widget=CKEditorUploadingWidget())
    class Meta:
        model = Author
        fields = '__all__'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'get_image',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'id')
    form = AuthorAdminForm
    def get_image(self, instance):
        return mark_safe(
            f'<img src="{instance.image.url}" alt="{instance.name}" width="150px" />'
        )
    get_image.short_description = 'Портрет'
    
    def get_books(self, instance):
        html = ''
        books = instance.books.all()
        print(books, 'dsfsdfsdfsdfdsfds')
        for book in books:
            html += f'<div style="margin-bottom: 10px"><a href="/admin/core/book/{book.id}/change/"><img src="{book.image.url}" width="40%"></a></div>'
        return mark_safe(html)
    get_books.short_description = 'книги автора'
    
    readonly_fields = ('get_image', 'get_books',)
    fields = (
        'name',
        'year',
        'information',
        'image',
        'get_image', 
        'get_books',       
    )
    
   
admin.site.site_header = 'Библиотека'   
    
# Register your models here.
