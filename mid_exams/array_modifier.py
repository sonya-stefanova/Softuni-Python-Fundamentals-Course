array = [int(num) for num in input().split(" ")]
command = input()

while command != "end":
    command = command.split(" ")
    action = command[0]

    if action == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]

    elif action == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])
        product = array[index_1] * array[index_2]
        array.pop(index_1)
        array.insert(index_1, product)

    elif action == "decrease":
        for el in range(len(array)):
            array[el]-=1

    command = input()
print(*array, sep = ", ")
