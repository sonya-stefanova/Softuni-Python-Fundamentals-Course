data = input().split(" ")
targets = list(map(int, data))
command = input()

while command != "End":
    index = int(command)

    if index >= len(targets):
        command = input()
        continue

    initial_value = targets[index]
    targets[index] = -1

    for index, current_value in enumerate(targets):
        if current_value != -1 and current_value > initial_value:
           targets[index]-=initial_value
        elif current_value !=-1 and current_value <= initial_value:
            targets[index] += initial_value
    command = input()
counter = targets.count(-1)
targets_as_string = list(map(str, targets))
targets_required_format = " ".join(targets_as_string)
print(f"Shot targets: {counter} -> {targets_required_format}")

