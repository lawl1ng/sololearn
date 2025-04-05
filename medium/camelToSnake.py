#camel to snake
camel = input()

def camel_to_snake(camel_case_string):
    snake_case_string = ""
    for i, c in enumerate(camel_case_string):
        if i == 0:
            snake_case_string += c.lower()
        elif c.isupper():
            snake_case_string += "_" + c.lower()
        else:
            snake_case_string += c
    return snake_case_string

print(camel_to_snake(camel))
