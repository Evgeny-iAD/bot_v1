import datetime

def dat():
    d = datetime.datetime.today().strftime("%H:%M ч.   %d.%m.%Y г.")
    return d