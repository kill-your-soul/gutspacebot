from datetime import datetime
import sqlite3


def timebuttons():
    if datetime.now().minute > 30:
        hour = int(datetime.now().hour) + 1
    else:
        hour = int(datetime.now().hour)

    hour = 10

    btime = []

    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()

    for i in range(3):
        av = cursor.execute(
            "SELECT * FROM availability WHERE time = ? OR time = ? OR time = ?",
            (hour + i - 1, hour + i, hour + i + 1),
        ).fetchall()

        if (av[0][1] + av[1][1] < 30) & (av[1][1] + av[2][1] < 30):
            btime.append(str(av[1][0]) + ":00")

    return btime


def bookingDB(txt):

    conn = sqlite3.connect("booking.db")
    cursor = conn.cursor()

    av = cursor.execute("SELECT * FROM availability WHERE time = ?", (txt.split(':')[0],)).fetchall()
    cursor.execute("UPDATE availability SET amount = ? WHERE time = ?", (av[0][1] + 1, av[0][0]))

    conn.commit()
    conn.close()
