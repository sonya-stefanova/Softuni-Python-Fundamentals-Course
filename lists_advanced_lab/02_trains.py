wagons = int(input())
train = [0]*wagons
command = input()
while command != "End":
    command_info = command.split(" ")
    action = command_info[0]

    if action == "add":
        number_of_people = int(command_info[1])
        train[-1] += number_of_people
    elif action == "insert":
        index = int(command_info[1])
        number_of_people = int(command_info[2])
        train[index] += number_of_people
    elif action == "leave":
        index = int(command_info[1])
        number_of_people = int(command_info[2])
        train[index] -= number_of_people
    command = input()
print(train)
