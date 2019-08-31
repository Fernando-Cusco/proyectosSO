from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre Categoria', max_length = 100, null = False, blank = False)
    estado = models.BooleanField('Caterogia activada/Categoria desactivada', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres del autor', max_length = 255, null = False, blank = False)
    apellidos = models.CharField('Apellidos del autor', max_length = 255, null = False, blank = False)
    direccion_facebook = models.URLField('Facebook', null = True, blank = True)
    direccion_twitter = models.URLField('Twitter', null = True, blank = True)
    direccion_instagram = models.URLField('Instagram', null = True, blank = True)
    direccion_web = models.URLField('Blog Personal', null = True, blank = True)
    correo = models.EmailField('Correo electronico', null = False, blank = False)
    estado = models.BooleanField('Autor Activo / Autor no activo', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos, self.nombres)


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo del Post', max_length = 100, null = False, blank = False)
    slug = models.CharField('Slug', max_length = 100, null = False, blank = False)
    descripcion = models.CharField('Descripcion', max_length = 110, blank = False, null = False)
    contenido = RichTextField('Contenido')
    imagen = models.URLField(max_length = 255, blank = False, null =False)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado / No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

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
