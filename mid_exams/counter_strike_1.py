total_energy = int(input())
command = input()
count_battle = 0

while command != 'End of battle':
    current_energy = int(command)

    if total_energy >= current_energy:
        total_energy -= current_energy
        count_battle += 1
    else:
        print(f"Not enough energy! Game ends with {count_battle} won battles and {total_energy} energy")
        break

    if count_battle % 3 == 0:
        total_energy += count_battle

    command = input()
else:
    print(f"Won battles: {count_battle}. Energy left: {total_energy}")