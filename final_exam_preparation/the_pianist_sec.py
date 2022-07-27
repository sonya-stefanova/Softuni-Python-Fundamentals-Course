n = int(input())
pieces = {}

for i in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {'composer': composer, 'key': key}

#defining the functions:
def add(collection, piece, composer, key):
    if piece in collection:
        print(f"{piece} is already in the collection!")
    else:
        collection[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return collection


def remove(collection, piece):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection


def change_key(collection, piece, new_key):
    if piece in collection:
        collection[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection


data = input()
while data != "Stop":
    commands = data.split("|")
    action = commands[0]
    if action == "Add":
        piece, composer, key = commands[1:]
        sonates = add(pieces, piece, composer, key)
    elif action == "Remove":
        piece = commands[1]
        sonates = remove(pieces, piece)
    elif action == "ChangeKey":
        piece = commands[1]
        new_key = commands[2]
        sonates = change_key(pieces, piece, new_key)
    data = input()

for piece, nested_dict in sonates.items():
    print(f'{piece} -> Composer: {nested_dict["composer"]}, Key: {nested_dict["key"]}')