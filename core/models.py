from django.db import models
from django.contrib.auth.models import User

MAX_LIMIT_SIZE = 2

def validated_image(file):
    if file.size > MAX_LIMIT_SIZE * 1048576:
        raise ValueError('Размер файла превышает  размера')
    else:
        return file

class Book(models.Model):

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        
    title = models.CharField(max_length=100, verbose_name='название книги')
    file  = models.FileField(verbose_name='книпга в pdf формате', 
                                                    upload_to='pdf_books/')
    genre = models.ForeignKey('Genre', verbose_name='жанр', 
                                                    on_delete=models.PROTECT)
    tags  = models.ManyToManyField("Tag", verbose_name='теги')
    image = models.ImageField(verbose_name='изображение', 
                        upload_to='books_images/', validators=[validated_image])
    description = models.TextField(verbose_name='описание')
    author = models.ForeignKey('Author', verbose_name='автор книги',
                                                    on_delete=models.CASCADE, related_name='books')
    likes = models.ManyToManyField(User, verbose_name='лайки', blank=True, related_name='favorite_books')
    views = models.PositiveIntegerField(verbose_name='просмотры', default=0)
    owner = models.ForeignKey(User, verbose_name='владелец', on_delete=models.CASCADE, null=True, related_name='books',)
    
    def __str__(self):
        return f'{self.title}'

 
class Genre(models.Model):
    
    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    title = models.CharField(max_length=50, verbose_name='название жанра')

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    title = models.CharField(max_length=50, verbose_name='название тега')

    def __str__(self):
        return self.title


class Author(models.Model):
    
    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    name = models.CharField(max_length=100, verbose_name='имя автора')
    year = models.CharField(max_length=9, verbose_name='период жизни')
    information = models.TextField(verbose_name='биография')
    image = models.ImageField(verbose_name='портрет автора', 
                        upload_to='authors_images', validators=[validated_image])

    def __str__(self):
        return self.name
# Create your models here.
