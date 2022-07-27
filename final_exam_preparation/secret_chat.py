concealed_message = input()

commands = input()


def insert_space(message, index):
    if index <= len(message) - 1:
        message = message[:index] + " " + message[index:]
        print(message)
        return message


def reverse(message, substring):
    if substring in message:
        cut_message = message.replace(substring, "", 1)
        rev_substring = substring[::-1]
        new_message = cut_message + rev_substring
        print(new_message)
        return new_message

    else:
        print("error")
        return message

    # elif instructions[0] == "Reverse":
    # substring_to_cut = instructions[1]
    # if substring_to_cut in concealed_message:
    #     substring_index = concealed_message.find(substring_to_cut)
    #     cutted_subtring = concealed_message[substring_index:substring_index + len(substring_to_cut)]
    #     reversed_cutted_substring = cutted_subtring[::-1]
    #     concealed_message = concealed_message[:substring_index] + concealed_message[substring_index + len(
    #         substring_to_cut):] + reversed_cutted_substring
    #     print(concealed_message)
    # else:
    #     print("error")

def change_all(message, substring, replacement):
    if substring in message:
        new_message = message.replace(substring, replacement)
        print(new_message)
        return new_message



while commands != "Reveal":
    commands = commands.split(":|:")
    action = commands[0]

    if action == "InsertSpace":
        index = int(commands[1])
        concealed_message = insert_space(concealed_message, index)
    elif action == "Reverse":
        substring = commands[1]
        concealed_message = reverse(concealed_message, substring)
    elif action == "ChangeAll":
        substring = commands[1]
        replacement = commands[2]
        concealed_message = change_all(concealed_message, substring, replacement)

    commands = input()
print(f"You have a new text message: {concealed_message}")
