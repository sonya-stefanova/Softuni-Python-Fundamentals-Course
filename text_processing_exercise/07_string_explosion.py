initial_string = input()
strength = 0
new_string = ""

for i in range(len(initial_string)):
    if initial_string[i] != ">" and strength > 0:
        strength -= 1
    elif initial_string[i] == ">":
        strength += int(initial_string[i + 1])
        new_string += initial_string[i]
    else:
        new_string += initial_string[i]

print(new_string)
