initial_energy = int(input())
command = input()
count_battle = 0

while command != 'End of battle':
    distance = int(command)

    if initial_energy >= distance:
        initial_energy -= distance
        count_battle += 1
    else:
        print(f"Not enough energy! Game ends with {count_battle} won battles and {initial_energy} energy")
        break

    if count_battle % 3 == 0:
        initial_energy += count_battle

    command = input()

else:
    print(f"Won battles: {count_battle}. Energy left: {initial_energy}")