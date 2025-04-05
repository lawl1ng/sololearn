numbers = [int(x) for x in input().split(" ")]

numbers2 = numbers.copy()

for number in numbers:
    if number % 2 != 0:
        numbers2.remove(number)


numbers2 = (" ").join([str(x) for x in numbers2])

print(numbers2)
