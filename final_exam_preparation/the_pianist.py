n = int(input())
pieces = {}

for i in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {'composer': composer, 'key': key}

data = input()
while not data == "Stop":
    commands = data.split("|")
    action = commands[0]

    if action == "Add":
        piece, composer, key = commands[1:]

        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = commands[1]

        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = commands[1]
        new_key = commands[2]

        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    data = input()

for piece, nested_dict in pieces.items():
    print(f'{piece} -> Composer: {nested_dict["composer"]}, Key: {nested_dict["key"]}')