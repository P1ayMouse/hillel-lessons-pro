from rest_framework import serializers

from apps.movies.models import Movie, Person, PersonMovie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'imdb_id', 'title_type', 'name', 'is_adult', 'year', 'genres']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'imdb_id', 'name', 'birth_year', 'death_year']


class PersonMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMovie
        fields = ['id', 'movie_id', 'person_id', 'order', 'category', 'job', 'characters']
    person_id = PersonSerializer()
