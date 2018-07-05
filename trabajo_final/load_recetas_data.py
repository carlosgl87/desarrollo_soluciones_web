from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import Receta
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from recetas.csv into our  model"

    def handle(self, *args, **options):
        if Receta.objects.exists():
            print('recetas data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading receta data for recetas available")
        for row in DictReader(open('./recetas.csv')):
            receta = Receta()
            receta.label = row['label']
            receta.healthLabels = row['healthLabels']
            receta.ingredientLines = row['ingredientLines']
            receta.calories = row['calories']
            receta.totalTime = row['totalTime']
            receta.Energy = row['Energy']
            receta.Fat = row['Fat']
            receta.Saturated = row['Saturated']
            receta.Carbs = row['Carbs']
            receta.Proteina = row['Proteina']
            receta.save()