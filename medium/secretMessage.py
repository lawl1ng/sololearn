#secret message
string = input().lower()

d = {
    "a":"z",
    "b":"y",
    "c":"x",
    "d":"w",
    "e":"v",
    "f":"u",
    "g":"t",
    "h":"s",
    "i":"r",
    "j":"q",
    "k":"p",
    "l":"o",
    "m":"n",
    "n":"m",
    "o":"l",
    "p":"k",
    "q":"j",
    "r":"i",
    "s":"h",
    "t":"g",
    "u":"f",
    "v":"e",
    "w":"d",
    "x":"c",
    "y":"b",
    "z":"a"
}

string = string.translate(str.maketrans(d))
    
print(string)

