import csv

from django.core.management import BaseCommand

from apps.movies.models import Movie


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str)
        parser.add_argument('--delimiter', type=str, default='\t')

    def handle(self, **options):
        file_name = options.get('file')

        with open(file_name) as f:
            csv_data = csv.reader(f, delimiter=options.get('delimiter', '\t'))
            for row in csv_data:
                row_data = {
                    'imdb_id': row[0],
                    'title_type': row[1],
                    'name': row[2],
                    'is_adult': row[4] == '1',
                    'year': f'{row[5]}-01-01' if row[5] != '\\N' else None,
                    'genres': row[8].split(',') if row[8] != '\\N' else [],
                }

                if row[1] not in ('short', 'movie'):
                    continue

                movie, created = Movie.objects.get_or_create(imdb_id=row_data['imdb_id'], defaults=row_data)
                if not created:
                    Movie.objects.filter(id=movie.id).update(**row_data)

                print(row_data)
