#version 1
action = input()

coffees = 0

action_to_lower = ['coding', 'movie', 'dog', 'cat']
action_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

while action != 'END':

    if action in action_to_lower:
        coffees += 1
    elif action in action_to_upper:
        coffees += 2

    action = input()

    if action == 'END':
        if coffees > 5:
            print('You need extra sleep')
        else:
            print(coffees)


#version2
command = ""
needed_coffee_counter = 0

while command.lower() != "end":
    command = input()
    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            needed_coffee_counter += 1
        else:
            needed_coffee_counter += 2
if needed_coffee_counter > 5:
    print("You need extra sleep")
else:
    print(needed_coffee_counter)