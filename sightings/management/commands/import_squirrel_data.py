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
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                question = squirrel.objects.create(
                        latitude = row[1],
                        longitude = row[0],
                        uniqueid = row[2],
                        shift = row[4],
                        Date = row[5],
                        Age = row[7],
                        furcolor = row[8],
                        location = row[12],
                        specificlocation = row[14],
                        running = row[15],
                        chasing = row[16],
                        climbing = row[17],
                        eating = row[18],
                        foraging = row[19],
                        otheractivities = row[20],
                        kuks = row[21],
                        quaas = row[22],
                        moans = row[23],
                        tailflags = row[24],
                        tailtwitches = row[25],
                        approaches = row[26],
                        indifferent = row[27],
                        runsfrom = row[28])
