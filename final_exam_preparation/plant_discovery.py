n = int(input())
plants ={}
for i in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {"Rarity": int(rarity), "Rating": []}

while True:
    commands = input()
    if commands == "Exhibition":
        break
    commands = commands.split(": ")
    
    action = commands.pop(0)
    data = commands[0].split(" - ")
    plant = data[0]

    if plant not in plants:
        print("error")
    else:
        if action == "Rate":
            rating = int(data[1])
            plants[plant]["Rating"].append(rating)
        elif action == "Update":
            new_rarity = int(data[1])
            plants[plant]["Rarity"] = new_rarity
        elif action == "Reset":
            plants[plant]["Rating"] = []

for values in plants.values():
    if len(values["Rating"]) > 0:
        values["Rating"] = (sum(values["Rating"]) / len(values["Rating"]))
    else:
        values["Rating"] = 0

print('Plants for the exhibition:')
for k, v in plants.items():
    print(f'- {k}; Rarity: {v["Rarity"]}; Rating: {v["Rating"]:.2f}')