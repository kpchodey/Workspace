import csv
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Webapp.settings'
from app.models import Revo
from app.models import Revo
def csvToDb(filename):
   for_import = []
   with open(data.csv) as repr_of_csv:
       data = repr_of_csv.read()
       python_csv_object = csv.reader(data)
       python_repr_of_csv = list(python_csv_object)
       for row in python_repr_of_csv:
         to_import = Revo()
         to_import.foo = row[0]
         to_import.bar = row[1]
         for_import.append(to_import)
# [model.save() for model in for_import]