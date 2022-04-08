import random

# Use this to generate some txt files

characters = "abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ"
line = []


def generate(lines, line_length):
    for i in range(lines):
        for y in range(line_length):
            line.append(random.choice(characters))
        line.append("\n")
    name = ""
    for i in range(6):
        name = name + random.choice(characters)
    with open(f'{name}.txt', 'a') as file:
        file.write("".join(line))

generate(10, 15)
# lines  ^   ^ characters in line