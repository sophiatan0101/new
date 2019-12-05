import csv
from django.core.management import BaseCommand
from sightings.models import squirrel
#import os
#from django.conf import settings
#base_dir = settings.BASE_DIR
#file_path = os.path.join(BASE_DIR, '/Users/lintan/Desktop/')



class Command(BaseCommand):
    help = 'Load a csv file into the database'
    def add_arguments(self,parser):
        parser.add_argument('csv_file')
        #parser.add_argument('', type=str)
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as f:
            reader = csv.DictReader(f)
            data = list(reader)
            for item in data:
            #reader = csv.reader(f, dialect='excel')
            #for row in reader:
                info = squirrel.objects.create(
                        latitude = item['Y'],
                        longitude = item['X'],
                        uniqueid = item['Unique Squirrel ID'],
                        shift = item['Shift'],
                        Date = item['Date'],
                        Age = item['Age'],
                        furcolor = item['Primary Fur Color'],
                        location = item['Location'],
                        specificlocation = item['Specific Location'],
                        running = item['Running'],
                        chasing = item['Chasing'],
                        climbing = item['Climbing'],
                        eating = item['Eating'],
                        foraging = item['Foraging'],
                        otheractivities = item['Other Activities'],
                        kuks = item['Kuks'],
                        quaas = item['Quaas'],
                        moans = item['Moans'],
                        tailflags = item['Tail flags'],
                        tailtwitches = item['Tail twitches'],
                        approaches = item['Approaches'],
                        indifferent = item['Indifferent'],
                        runsfrom = item['Runs from'])
                info.save()
