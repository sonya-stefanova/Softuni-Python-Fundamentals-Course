health = 100
bitcoins = 0
pass_through_all_rooms = True

dungeon_room = input().split("|")
best_room = 0
for room in dungeon_room:
    best_room +=1
    room_info = room.split((" "))
    command = room_info[0]
    current_number = int(room_info[1])

    if command == "potion":
        amount = current_number
        if health + amount >= 100:
            amount = 100 - health
        health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        amount = current_number
        bitcoins += amount
        print(f"You found {bitcoins} bitcoins.")
    else:
        attack = current_number
        health -= attack
        monster = command
        if health > 0:
            print(f"You slayed {monster}")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {best_room}")
            pass_through_all_rooms = False
            exit()
if pass_through_all_rooms:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
