# days between dates
import datetime

date1 = input()
date2 = input()

def convert(date_string):
    if " " in date_string:
        format = "%B %d, %Y"
    else:
        format = "%m/%d/%Y"
    dt = datetime.datetime.strptime(date_string, format).date()
    return dt

date1 = convert(date1)
date2 = convert(date2)

res = str(date2 - date1).split(" ")

print(res[0])
