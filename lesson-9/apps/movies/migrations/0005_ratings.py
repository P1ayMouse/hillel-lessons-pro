# Generated by Django 4.1.7 on 2023-04-02 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_alter_movie_genres_alter_movie_imdb_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ratings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("average_rating", models.FloatField(verbose_name="Rating")),
                ("num_votes", models.IntegerField(verbose_name="Num votes")),
                (
                    "movie_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="movies.movie"
                    ),
                ),
            ],
        ),
    ]