from django.shortcuts import render

# Create your views here.

from apps.movies.models import Movie
from django.views.generic import ListView


class MovieListView(ListView):
    model = Movie
