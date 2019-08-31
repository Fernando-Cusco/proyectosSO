from django.contrib import admin
from .models import  Libro
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro


class LibroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['book_title']
    list_display = ['book_title', 'book_desc']
    resource_class = LibroResource


admin.site.register(Libro, LibroAdmin)
