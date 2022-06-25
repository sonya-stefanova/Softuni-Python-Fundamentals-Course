notes = [0]*10
command = input()

while command != "End":
    data = command.split("-")
    priority_index = int(data[0])-1
    to_do = data[1]
    notes.pop(priority_index)
    notes.insert(priority_index, to_do)
    command = input()
result = [element for element in notes if element!=0]
print(result)