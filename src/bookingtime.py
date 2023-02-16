from datetime import datetime


def timebuttons():
    hour = datetime.now().hour
    min = datetime.now().minute
    btime = []

    if min > 30:
        for i in range(3):
            btime.append(str(hour + i + 1) + ":00")
    else:
        for i in range(3):
            btime.append(str(hour + i) + ":00")

    return btime
