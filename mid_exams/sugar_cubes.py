sugar_cubes = list(map(int, input().split(" ")))
line = input()

while line != "Mort":
    commands = line.split(" ")
    action = commands[0]
    value = int(commands[1])

    if action == "Add":
        sugar_cubes.append(value)

    elif action == "Remove":
        if value in sugar_cubes:
            sugar_cubes.remove(value)

    elif action == "Replace":
        replacement = commands[2]
        if value in sugar_cubes:
            index = sugar_cubes.index(value)
            sugar_cubes.insert(index, replacement)
            sugar_cubes.pop(value)

    elif action == "Collapse":
        sugar_cubes = [n for n in sugar_cubes if n >= value]

    line = input()

print(" ".join(map(str, sugar_cubes)))