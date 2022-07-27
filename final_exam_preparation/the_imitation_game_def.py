main_string = input()

command = input()


def move_sting(n, string):
    return string[n:] + string[:n]


def insert_string(i, value, string):
    return string[:i] + value + string[i:]


def change_all(substring, replacement, string):
    return string.replace(substring, replacement)


while not command == "Decode":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split("|")]
    if command_type == "Move":
        n = info[0]
        main_string = move_sting(n, main_string)
    else:
        i_or_substring, value_or_replacement = info
        if command_type == "Insert":
            main_string = insert_string(i_or_substring, value_or_replacement, main_string)
        elif command_type == "ChangeAll":
            main_string = change_all(i_or_substring, value_or_replacement, main_string)

    command = input()

print(f"The decrypted message is: {main_string}")