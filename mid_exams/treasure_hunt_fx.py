def loot(loots, data):
    data.pop(0)
    for item in data:
        if item not in loots:
            loots.insert(0, item)
    return loots


def drop(loots, data):
    idx = int(data[1])
    if idx < len(loots):
        removed_loot = loots.pop(idx)
        loots.append(removed_loot)
    return loots


def steal(loots, data):
    count_stolen_items = int(data[1])
    if count_stolen_items >= len(loots):
        stolen_items = loots
        print(', '.join(stolen_items))
        print(f"Failed treasure hunt.")
        exit()
    else:
        stolen_items = loots[-count_stolen_items:]
        del loots[-count_stolen_items:]
        print(', '.join(stolen_items))
    return loots


loots = input().split("|")
command = input()
is_empty = False

while command != "Yohoho!":
    data = command.split()
    action = data[0]
    if action == "Loot":
        loots = loot(loots, data)
    elif action == "Drop":
        loots = drop(loots, data)
    elif action == "Steal":
        loots = steal(loots, data)
    command = input()

if len(loots)>0:
    sum_loots_length = sum([len(loot) for loot in loots])
    average = sum_loots_length / len(loots)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
