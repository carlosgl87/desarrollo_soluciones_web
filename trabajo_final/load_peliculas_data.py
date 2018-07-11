from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import Peliculas
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from peliculas.csv into our  model"

    def handle(self, *args, **options):
        if Peliculas.objects.exists():
            print('peliculas data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading pelicula data for peliculas available")
        for row in DictReader(open('./peliculas.csv')):
            pelicula = Peliculas()
            pelicula.Title = row['Title']
            pelicula.Year = row['Year']
            pelicula.Rated = row['Rated']
            pelicula.Released = row['Released']
            pelicula.Genre = row['Genre']
            pelicula.Director = row['Director']
            pelicula.Plot = row['Plot']
            pelicula.imdbRating = row['imdbRating']
            pelicula.Metascore = row['Metascore']
            pelicula.Country = row['Country']
            pelicula.save()