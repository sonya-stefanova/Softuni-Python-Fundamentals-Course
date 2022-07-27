n = int(input())
plants = {}
for i in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant not in plants:
        plants[plant] = {"rarity": 0, "rating": []}
    plants[plant]['rarity'] = rarity

data = input()
while data!= "Exhibition":
    data = data.split(": ")
    command = data[0]
    plant_data = data[1]
    plant_data = plant_data.split(" - ")
    plant = plant_data[0]

    if plant not in plants.keys():
        print("error")
        continue

    if command == "Rate":
        rating = int(plant_data[1])
        plants[plant]["rating"].append(rating)
    elif command == "Update":
        new_rarity = int(plant_data[1])
        plants[plant]['rarity'] = new_rarity
    elif command == "Reset":
        plants[plant]["rating"] = []
    else:
        print("error")

    data = input()

plant_discovery = {}
for plant in plants:
    if sum(plants[plant]['rating']) > 0:
        average_rating = sum(plants[plant]['rating']) / len(plants[plant]['rating'])
    else:
        average_rating = 0
    plant_discovery[plant] = {'rarity': plants[plant]['rarity'], 'average': average_rating}

print("Plants for the exhibition:")
for key, value in plant_discovery.items():
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['average']:.2f}")