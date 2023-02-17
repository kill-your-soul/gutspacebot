from . import sh


async def person_add(name, time):
    
    h = {
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

    wks = sh.worksheet_by_title('Занятость')
    all_records = wks.get_all_records()
    rec_col = []
    for i in all_records:
        rec_col.append(i[time])
        
    try:
        while True:
            rec_col.remove('')
    except ValueError:
        pass

    wks.update_value(f"{h.get(time)}{len(rec_col)+2}", name)
