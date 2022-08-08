commands = input()
dwarfs = {}

while commands != "Once upon a time":
    commands = commands.split(" <:> ")
    name, hat_color, physics = commands[0], commands[1], int(commands[2])

    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}
    if name not in dwarfs[hat_color]:
        dwarfs[hat_color][name] = 0
    if name in dwarfs[hat_color]:
        if physics > dwarfs[hat_color][name]:
            dwarfs[hat_color][name] = physics

    commands = input()

sorted_dwarfs = []
for color in dwarfs.keys():
    for name, physics in dwarfs[color].items():
        total_count = len(dwarfs[color].keys())
        sorted_dwarfs.append([physics, total_count, {color: [name]}])

for data in sorted(sorted_dwarfs, key=lambda kv: (-kv[0], -kv[1])):
    physics = data[0]
    for color, names in data[2].items():
        for name in names:
            print(f"({color}) {name} <-> {physics}")