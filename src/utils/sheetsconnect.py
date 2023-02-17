from . import sh

def person_add():

    wks = sh.worksheet_by_title('Занятость')
    wks.update_value("A2", "42")