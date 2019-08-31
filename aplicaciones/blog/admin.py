from django.contrib import admin
from .models import Autor, Categoria, Post, Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']                          #agregar barra de busqueda dentro del modelo Categoria
    list_display = (                                     #atributos que queremos mostrar en el admin
        'nombre',
        'estado',
        'fecha_creacion',
    )
    resource_class = CategoriaResource                  #Agregamos el boton de import y export

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres']
    list_display = ('nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion')
    resource_class = AutorResource

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ['titulo', 'descripcion', 'autor', 'categoria', 'fecha_creacion']
    resource_class = PostResource

class LibroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['book_title']
    list_display = ['book_title', 'book_desc']
    resource_class = LibroResource


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Libro, LibroAdmin)
