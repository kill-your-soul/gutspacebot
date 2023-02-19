import os
import pygsheets
import sqlite3

conn = sqlite3.connect("booking.db")
cursor = conn.cursor()

cursor.execute("UPDATE availability SET amount = 0")

conn.commit()
conn.close()

service_file = os.environ["service_file"]
gc = pygsheets.authorize(service_file=service_file)
sheetname = "SutSpace занятость"
sh = gc.open(sheetname)

wks = sh.worksheet_by_title("VK_ID")
wks1 = sh.worksheet_by_title("Занятость")

wks.clear(start='A2', end='L26')
wks1.clear(start='A2', end='L26')
