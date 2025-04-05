# military time
intime = input()

from datetime import datetime 

def convert24(time): 
    # Parse the time string into a datetime object 
    t = datetime.strptime(time, '%I:%M %p') 
    # Format the datetime object into a 24-hour time string 
    return t.strftime('%H:%M') 

print(convert24(intime))
