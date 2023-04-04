import os
import pygsheets
import threading
from time import sleep
from clearAll import clearAll

err = [0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23, 24]

time_voc = {
    "9:00": "A",
    "10:00": "B",
    "11:00": "C",
    "12:00": "D",
    "13:00": "E",
    "14:00": "F",
    "15:00": "G",
    "16:00": "H",
    "17:00": "I",
    "18:00": "J",
    "19:00": "k",
    "20:00": "L",
}

service_file = os.environ["service_file"]
gc = pygsheets.authorize(service_file=service_file)
sheetname = "SutSpace занятость"
sh = gc.open(sheetname)

threading.Thread(target=clearAll, daemon=True).start()
