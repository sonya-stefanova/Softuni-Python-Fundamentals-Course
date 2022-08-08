main_string = input()
def insert_space(main_string, i):
    main_string = main_string[:i]+" "+main_string[i:]
    print(main_string)
    return main_string

def reverse(main_string, substring):
    if substring not in main_string:
        print("error")
        return main_string
    else:
        cut_out_message = main_string.replace(substring,"",1)
        rev_substring = cut_out_message[::-1]
        main_string = cut_out_message + rev_substring
        print(main_string)
        return main_string

def change_all(main_string, sub, replacement):
    main_string = main_string.replace(sub, replacement)
    print(main_string)
    return main_string

commands = input()
while commands!= "Reveal":
    commands = commands.split(":|:")
    action = commands[0]

    if action =="InsertSpace":
        i = int(commands[1])
        main_string = insert_space(main_string, i)
    elif action == "Reverse":
        substring = commands[1]
        main_string = insert_space(main_string, substring)
    elif action =="ChageAll":
        substring = commands[1]
        replacement = commands[2]
        main_string = insert_space(main_string, substring, replacement)
    commands = input()

print(f"You have a new text message: {main_string}")