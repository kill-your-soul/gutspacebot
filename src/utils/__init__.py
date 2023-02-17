import os
import pygsheets


service_file = os.environ["service_file"]
gc = pygsheets.authorize(service_file=service_file)
sheetname = "SutSpace занятость"
sh = gc.open(sheetname)
