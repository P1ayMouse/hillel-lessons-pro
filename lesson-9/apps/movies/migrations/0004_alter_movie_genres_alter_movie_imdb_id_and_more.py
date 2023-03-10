# Generated by Django 4.1.6 on 2023-02-19 19:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_title_type_alter_person_birth_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255, verbose_name='Genres'), size=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(max_length=255, verbose_name='Id of IMDB'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title_type',
            field=models.CharField(choices=[('short', 'Short Movie'), ('movie', 'Movie')], max_length=255, verbose_name='Type of title'),
        ),
        migrations.AlterField(
            model_name='person',
            name='imdb_id',
            field=models.CharField(max_length=255, verbose_name='Id of IMDB'),
        ),
        migrations.AlterField(
            model_name='personmovie',
            name='category',
            field=models.CharField(max_length=255, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='personmovie',
            name='job',
            field=models.CharField(max_length=255, verbose_name='Job'),
        ),
    ]
