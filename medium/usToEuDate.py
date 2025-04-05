#convert us date to eu date
date = str(input())

month = {"January":"1",
        "February":"2",
        "March":"3",
        "April":"4",
        "May":"5",
        "June":"6",
        "July":"7",
        "August":"8",
        "September":"9",
        "October":"10",
        "November":"11",
        "December":"12"}

if "/" in date:
    date = date.split("/")
else:
    date = date.split(" ")
    date[1] = date[1][:-1]
    for word, number in month.items():
        date[0] = date[0].replace(word, number)
        
date = (
        date[1] + "/" +
        date[0] + "/" +
        date[2])
    

print(date)

