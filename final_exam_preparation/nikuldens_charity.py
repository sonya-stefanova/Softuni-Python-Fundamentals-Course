main_string = input()


def is_valid_index(main_string, index):
    if 0 <= index < len(main_string):
        return True
    return False


def replace(main_string, current_char, new_char):
    main_string = main_string.replace(current_char, new_char, -1)
    print(main_string)
    return main_string


def cut(main_string, start_i, end_i):
    if is_valid_index(main_string, start_i) and is_valid_index(end_i):
        main_string = main_string[:start_i] + main_string[end_i:]
        print(main_string)
        return main_string
    else:
        print("Invalid indexes!")
        return main_string


def make(main_string, state):
    if "Upper" in state:
        main_string = main_string.upper()
        print(main_string)
    elif "Lower" in state:
        main_string = main_string.lower()
        print(main_string)
    return main_string


def check(main_string, string):
    if string in main_string:
        print(f"Message contains {string}")
    else:
        print(f'Message doesn\'t contain {string}')
    return main_string


def sum(main_string, start_index, end_index):
    if is_valid_index(main_string, start_index) and is_valid_index(main_string, end_index):
        substring = main_string[start_index:(end_index + 1)]
        substring_ascii_values = [ord(ch) for ch in substring]
        sum_substring_values = sum(substring_ascii_values)
    else:
        print("Invalid indexes!")
    return main_string

command_info = input().split(" ")
while command_info[0] != "Finish":

    if command_info[0] == "Replace":
        current_char = command_info[1]
        new_char = command_info[2]
        main_string = replace(main_string, current_char, new_char)
    elif command_info[0] == "Cut":
        start_index = int(command_info[1])
        end_index = int(command_info[2])
        main_string = cut(main_string, start_index, end_index)
    elif command_info[0] == "Make":
        state = command_info[2]
        main_string = make(main_string, state)
    elif command_info[0] == "Check":
        string = command_info[1]
        main_string = check(main_string, string)
    elif command_info[0] == "Sum":
        start_i = int(command_info[1])
        end_i = int(command_info[2])
        main_string = sum(main_string, start_i, end_i)

        command = input()
