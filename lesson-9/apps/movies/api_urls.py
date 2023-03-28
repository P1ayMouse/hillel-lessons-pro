from django.urls import path

from apps.movies.api_views import MovieListCreateView, MoviesRetrieveUpdateDestroyView, \
    PersonListCreateView, PersonsRetrieveUpdateDestroyView, \
    PersonMovieListCreateView, PersonMoviesRetrieveUpdateDestroyView

app_name = 'api-movies'

urlpatterns = [
    path('movies/', MovieListCreateView.as_view()),
    path('movies/<str:pk>/', MoviesRetrieveUpdateDestroyView.as_view()),
    path('persons/', PersonListCreateView.as_view()),
    path('persons/<str:pk>/', PersonsRetrieveUpdateDestroyView.as_view()),
    path('personmovies/', PersonMovieListCreateView.as_view()),
    path('personmovies/<str:pk>/', PersonMoviesRetrieveUpdateDestroyView.as_view()),
]
