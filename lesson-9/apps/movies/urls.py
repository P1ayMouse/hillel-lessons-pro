from django.urls import path

from apps.movies.views import MovieListView

app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view())
]
