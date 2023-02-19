from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Movie(models.Model):
    class TitleType(models.TextChoices):
        short = ('short', _('Short Movie'))
        movie = ('movie', _('Movie'))

    imdb_id = models.CharField(_('Id of IMDB'), max_length=255)
    title_type = models.CharField(_('Type of title'), max_length=255, choices=TitleType.choices)
    name = models.CharField(_('Name'), max_length=255)
    is_adult = models.BooleanField(_('Is adult'), default=False)
    year = models.DateField(_('Year'), null=True)
    genres = ArrayField(models.CharField(_('Genres'), max_length=255))


class Person(models.Model):
    imdb_id = models.CharField(_('Id of IMDB'), max_length=255)
    name = models.CharField(_('Name'), max_length=255)
    birth_year = models.DateField(_('Birth year'), null=True)
    death_year = models.DateField(_('Death year'), null=True)


class PersonMovie(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT)
    person_id = models.ForeignKey(Person, on_delete=models.PROTECT)
    order = models.IntegerField(_('Order'))
    category = models.CharField(_('Category'), max_length=255)
    job = models.CharField(_('Job'), max_length=255)
    characters = ArrayField(models.CharField(_('Characters'), max_length=255))
