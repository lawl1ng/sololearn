#day of week
import datetime

dt = input()

def convert(date_string):
    if " " in date_string:
        format = "%B %d, %Y"
    else:
        format = "%m/%d/%Y"
    dt = datetime.datetime.strptime(date_string, format).date()
    dt = dt.strftime("%A")
    return dt

print(convert(dt))
