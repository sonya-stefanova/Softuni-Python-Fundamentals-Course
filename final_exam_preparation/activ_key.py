activation_key = input()


def contain(line, substring):
    if substring in line:
        print(f"{line} contains {substring}")
        return line
    else:
        print("Substring not found!")
        return line


def flip_part(line, action, index_1, index_2):
    index_1 = int(index_1)
    index_2 = int(index_2)
    flipping_part = line[index_1:index_2]
    if action == "Upper":
        line = line.replace(flipping_part, flipping_part.upper())
        print(line)
        return line
    elif action == "Lower":
        line = line.replace(flipping_part, flipping_part.lower())
        print(line)
        return line


def slice_part(line, index_1, index_2):
    index_1 = int(index_1)
    index_2 = int(index_2)
    part_for_slice = line[index_1:index_2]
    line = line.replace(part_for_slice, "")
    print(line)
    return line

command = input()
while command!= "Generate":

    instruction = command.split(">>>")

    if instruction[0] == "Contains":
        activation_key = contain(activation_key, instruction[1])
    elif instruction[0] == "Flip":
        activation_key = flip_part(activation_key, instruction[1], instruction[2], instruction[3])
    elif instruction[0] == "Slice":
        activation_key = slice_part(activation_key, instruction[1], instruction[2])
    command = input()
print(f"Your activation key is: {activation_key}")