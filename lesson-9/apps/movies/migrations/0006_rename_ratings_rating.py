# Generated by Django 4.1.7 on 2023-04-02 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_ratings"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Ratings",
            new_name="Rating",
        ),
    ]
