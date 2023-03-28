from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.movies.models import Movie, Person, PersonMovie
from apps.movies.serializers import MovieSerializer, PersonSerializer, PersonMovieSerializer


class MovieListCreateView(ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer
    search_fields = ['^name', ]

    def get_queryset(self):
        queryset = Movie.objects.all()

        if order_by := self.request.query_params.get('order_by'):
            queryset = queryset.order_by(order_by)

        return queryset


class MoviesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class PersonListCreateView(ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PersonSerializer
    search_fields = ['=id']

    def get_queryset(self):
        queryset = Person.objects.all()

        if order_by := self.request.query_params.get('order_by'):
            queryset = queryset.order_by(order_by)

        return queryset


class PersonsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonMovieListCreateView(ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PersonMovieSerializer
    search_fields = ['=movie_id__id']

    def get_queryset(self):
        queryset = PersonMovie.objects.all()

        if order_by := self.request.query_params.get('order_by'):
            queryset = queryset.order_by(order_by)

        return queryset


class PersonMoviesRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonMovieSerializer
    queryset = PersonMovie.objects.all()


