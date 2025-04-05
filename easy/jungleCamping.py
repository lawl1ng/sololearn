#jungle camping
animals = input()
animals = animals.split(" ")

result = ""
i = 0

while i <= (len(animals) - 1):
    if animals[i] == 'Grr':
        result = result + " Lion"
    if animals[i] == 'Rawr':
        result = result + " Tiger"
    if animals[i] == 'Ssss':
        result = result + " Snake"
    if animals[i] == 'Chirp':
        result = result + " Bird"
    i += 1

print(result[1:])
