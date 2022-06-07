initial_energy = int(input())
counter_battles = 0
command = " "
while initial_energy >= 0:
    command = input()

    if command == "End of battle":
        break
    else:
        current_distance = int(command)

    if initial_energy >= current_distance:
        counter_battles += 1
        initial_energy -= current_distance
    else:
        print(f"Not enough energy! Game ends with {counter_battles} won battles and {initial_energy} energy")
        break

    if counter_battles % 3 == 0:
        initial_energy += counter_battles

if command == "End of battle" or initial_energy >= 0:
    print(f"Won battles: {counter_battles}. Energy left: {initial_energy}")
