# Generated by Django 4.1.6 on 2023-02-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(verbose_name='Birth Date'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]