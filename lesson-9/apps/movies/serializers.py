from django.db.models import Avg
from rest_framework import serializers

from apps.movies.models import Movie, Person, PersonMovie, Rating


class MovieSerializer(serializers.ModelSerializer):
    directors = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'imdb_id', 'title_type', 'name', 'is_adult', 'year', 'genres', 'directors', 'average_rating']

    def get_directors(self, obj):
        return obj.personmovie_set.filter(category__iexact='director').values_list("person_id__name", flat=True)

    def get_average_rating(self, obj):
        return obj.rating_set.values_list("average_rating", flat=True).get()


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'imdb_id', 'name', 'birth_year', 'death_year']


class PersonMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonMovie
        fields = ['id', 'movie_id', 'person_id', 'order', 'category', 'job', 'characters']
    person_id = PersonSerializer()


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'movie_id', 'average_rating', 'num_votes']
