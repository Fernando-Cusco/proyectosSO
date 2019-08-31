# Generated by Django 2.2.2 on 2019-07-19 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190705_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_authors', models.CharField(blank=True, max_length=255, null=True, verbose_name='Autor del libro')),
                ('book_desc', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Descripcion libro')),
                ('book_edition', models.CharField(blank=True, max_length=255, null=True, verbose_name='Edicion del libro')),
                ('book_format', models.CharField(blank=True, max_length=255, null=True, verbose_name='Formato del libro')),
                ('book_isbn', models.CharField(blank=True, max_length=255, null=True, verbose_name='Isbn del libro')),
                ('book_pages', models.CharField(blank=True, max_length=255, null=True, verbose_name='Numero de pagina del libro')),
                ('book_rating', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calificacion del libro')),
                ('book_rating_count', models.CharField(blank=True, max_length=255, null=True, verbose_name='Calificacion conteo del libro')),
                ('book_review_count', models.CharField(blank=True, max_length=255, null=True, verbose_name='Review del libro')),
                ('book_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Titulo del libro')),
                ('genres', models.CharField(blank=True, max_length=255, null=True, verbose_name='Genero del libro')),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]