def collect(sequence:list, item:str):
    if item not in sequence:
        items.append(item)
    return sequence


def drop(sequence:list, item:str):
    if item in sequence:
        items.remove(item)
    return sequence


def combine_items(sequence:list, item:str):
    [old_item, new_item] = item.split(":")
    for i in range(len(sequence)):
        if sequence[i] == old_item:
            items.insert(i+1, new_item)
    return sequence


def renew(sequence:list, item:str):
    for i in range(len(items)):
        if sequence[i] == item:
            sequence.pop(i)
            sequence.append(item)
    return sequence


items = input().split(", ")

while True:
    commands = input()
    if commands == "Craft!":
        break
    [command, item] = commands.split(" - ")
    if command == "Collect":
        items = collect(items, item)
    elif command == "Drop":
        items = drop(items, item)
    elif command == "Combine Items":
        items = combine_items(items, item)
    elif command == "Renew":
        renew(items, item)

print(", ".join(items))