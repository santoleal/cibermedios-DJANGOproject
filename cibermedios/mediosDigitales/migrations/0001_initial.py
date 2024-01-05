# Generated by Django 5.0.1 on 2024-01-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cibermedios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('anio_creacion', models.DateField()),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investigaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autores', models.CharField(max_length=200)),
                ('anio_publicacion', models.DateField()),
                ('pais_referencia', models.CharField(max_length=200)),
                ('resumen', models.CharField(blank=True, max_length=500, null=True)),
                ('palabras_claves', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Investigadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('biografia', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
