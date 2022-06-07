groceries = input().split("!")
command = input()

while command != "Go Shopping!":
    shopping_command = command.split()

    if "Urgent" in shopping_command:
        for i in range(len(groceries)):
            if shopping_command[1] not in groceries:
                groceries.insert(0, shopping_command[1])
    elif "Unnecessary" in shopping_command:
        for i in range(len(groceries)):
            if shopping_command[1] in groceries:
                groceries.remove(shopping_command[1])
    elif "Correct" in shopping_command:
        for i in range(len(groceries)):
            if shopping_command[1] in groceries:
                groceries[groceries.index(shopping_command[1])] = shopping_command[2]
    elif "Rearrange" in shopping_command:
        for i in range(len(groceries)):
            if shopping_command[1] in groceries:
                index = groceries.index(shopping_command[1])
                groceries.pop(index)
                groceries.append(shopping_command[1])
    command = input()
result = ", ".join(groceries)
print(result)
