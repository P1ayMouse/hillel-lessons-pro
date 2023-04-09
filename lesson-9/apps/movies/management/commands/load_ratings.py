import csv

from django.core.management import BaseCommand

from apps.movies.models import Movie, Rating


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)
        parser.add_argument('--delimiter', type=str, default='\t')

    def handle(self, **options):
        file_name = options.get('file')

        with open(file_name) as f:
            csv_data = csv.reader(f, delimiter=options.get('delimiter', '\t'))
            for row in csv_data:
                movie = Movie.objects.filter(imdb_id=row[0]).first()
                if movie:
                    row_data = {
                        'movie_id': movie,
                        'average_rating': row[1],
                        'num_votes': row[2],
                    }

                    ratings, created = Rating.objects.update_or_create(movie_id=movie, defaults=row_data)

                    print(row_data)
