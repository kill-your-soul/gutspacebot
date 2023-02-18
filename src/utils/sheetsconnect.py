from . import sh, time_voc


async def person_add(name, time):
    
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

    wks.update_value(f"{time_voc.get(time)}{len(rec_col)+2}", name)

async def bookingCheck(time, vk_id):

    wks = sh.worksheet_by_title('VK_ID')
    all_records = wks.get_all_records()
    rec_col = []
    for i in all_records:
        rec_col.append(i[time])

    try:
        while True:
            rec_col.remove('')
    except ValueError:
        pass

    if vk_id in rec_col:
        return True
    
    wks.update_value(f"{time_voc.get(time)}{len(rec_col)+2}", vk_id)
    return False