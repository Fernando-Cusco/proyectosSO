from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

#book_rating,book_rating_count,book_review_count,book_title,genres,image_url

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    book_authors = models.CharField('Autor del libro', max_length = 255, null = True, blank =  True)
    book_desc = models.CharField('Descripcion libro', max_length = 1100, null = True, blank =  True)
    book_edition = models.CharField('Edicion del libro', max_length = 255, null = True, blank =  True)
    book_format = models.CharField('Formato del libro', max_length = 255, null = True, blank =  True)
    book_isbn = models.CharField('Isbn del libro', max_length = 255, null = True, blank =  True)
    book_pages = models.CharField('Numero de pagina del libro', max_length = 255, null = True, blank =  True)
    book_rating = models.CharField('Calificacion del libro', max_length = 255, null = True, blank =  True)
    book_rating_count = models.CharField('Calificacion conteo del libro', max_length = 255, null = True, blank =  True)
    book_review_count = models.CharField('Review del libro', max_length = 255, null = True, blank =  True)
    book_title = models.CharField('Titulo del libro', max_length = 255, null = True, blank =  True)
    genres = models.CharField('Genero del libro', max_length = 255, null = True, blank =  True)
    image_url = models.URLField(max_length = 255, blank = True, null =True)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.book_title
