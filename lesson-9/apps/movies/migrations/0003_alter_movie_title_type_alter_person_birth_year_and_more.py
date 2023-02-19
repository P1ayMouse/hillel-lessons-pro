# Generated by Django 4.1.6 on 2023-02-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title_type',
            field=models.CharField(choices=[('short', 'Short Movie'), ('movie', 'Movie')], max_length=80, verbose_name='Type of title'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_year',
            field=models.DateField(null=True, verbose_name='Birth year'),
        ),
        migrations.AlterField(
            model_name='person',
            name='death_year',
            field=models.DateField(null=True, verbose_name='Death year'),
        ),
    ]
