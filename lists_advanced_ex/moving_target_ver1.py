def shoot(sequence, i, v):
    if 0 <= i < len(sequence):
        sequence[i] -= v
        if sequence[i] <= 0:
            sequence.pop(i)
    return sequence


def add(sequence, i, v):
    if 0 <= i < len(sequence):
        sequence.insert(i, v)
    else:
        print("Invalid placement!")
    return sequence


def strike(sequence, i, v):
    left_i = i-v
    right_i = i+v
    if left_i >= 0 and right_i < len(sequence):
        left_part = sequence[:left_i]
        right_part = sequence[right_i+1:]
        sequence = left_part+right_part
    else:
        print("Strike missed!")
    return sequence


targets = [int(i) for i in input().split()]

while True:
    commands = input()
    if commands == "End":
        break

    action, index, value = commands.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        targets = shoot(targets, index, value)
    elif action == "Add":
        targets = add(targets, index, value)
    elif action == "Strike":
        targets = strike(targets, index, value)

print("|".join([str(i) for i in targets]))

