pirates_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health_capacity = int(input())
command = input()

while command != "Retire":
    command = command.split(" ")
    action = command[0]

    if action == "Fire":
        idx = int(command[1])
        damage = int(command[2])
        if 0<= idx < len(warship):
            warship[idx] -= damage
            if warship[idx] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()


    elif action == "Defend":
        start_idx = int(command[1])
        end_idx = int(command[2])
        damage = int(command[3])

        if 0 <= start_idx < end_idx < len(pirates_ship):
            for i in range(start_idx, end_idx + 1):
                pirates_ship[i] -= damage
                if pirates_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif action == "Repair":
        idx = int(command[1])
        health = int(command[2])
        if 0<= idx < len(pirates_ship):
            pirates_ship[idx] += health
            if pirates_ship[idx] > max_health_capacity:
                pirates_ship[idx] = max_health_capacity

    elif action == "Status":
        need_repair_soon = list(filter(lambda i: i< (0.2 * max_health_capacity), pirates_ship))
        count = len(need_repair_soon)
        print(f"{count} sections need repair.")
    command = input()

print(f"Pirate ship status: {sum(pirates_ship)}")
print(f"Warship status: {sum(warship)}")
