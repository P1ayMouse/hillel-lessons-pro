import csv
import ast

from django.core.management import BaseCommand

from apps.movies.models import Movie, Person, PersonMovie


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
                person = Person.objects.filter(imdb_id=row[2]).first()
                if person:
                    row_data = {
                        'movie_id': movie,
                        'person_id': person,
                        'order': row[1],
                        'category': row[3],
                        'job': row[4] if row[4] != '\\N' else None,
                        'characters': ast.literal_eval(row[5]) if row[5] != '\\N' else [],
                    }

                    person_movie, created = PersonMovie.objects.update_or_create(movie_id=movie, person_id=person,
                                                                                 defaults=row_data)

                    print(row_data)
