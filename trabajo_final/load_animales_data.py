from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import Animales
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from animales.csv into our  model"

    def handle(self, *args, **options):
        if Animales.objects.exists():
            print('animales data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading animales data for animales available")
        for row in DictReader(open('./animales.csv')):
            animal = Animales()
            animal.genus_name = row['genus_name']
            animal.scientific_name = row['scientific_name']
            animal.family_name = row['family_name']
            animal.order_name = row['order_name']
            animal.class_name = row['class_name']
            animal.phylum_name = row['phylum_name']
            animal.kingdom_name = row['kingdom_name']
            animal.infra_name = row['infra_name']
            animal.population = row['population']
            animal.category = row['category']
            animal.save()