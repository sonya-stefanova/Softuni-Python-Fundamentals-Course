message = input()
message_lst = [letter for letter in message]

item = None

while True:
    command = input().split('|')
    action = command[0]

    if action == 'Decode':
        break

    if action == 'Move':
        item = message_lst[0:int(command[1])]
        del message_lst[0:int(command[1])]
        for letter in item:
            message_lst.append(letter)

    if action == 'Insert':
        first_part = message_lst[:int(command[1])]
        second_part = message_lst[int(command[1]):len(message_lst)]
        message_lst = []
        for letter in first_part:
            message_lst.append(letter)
        for letter in command[2]:
            message_lst.append(letter)
        for letter in second_part:
            message_lst.append(letter)

    if action == 'ChangeAll':
        message_lst[:] = [x if x != command[1] else command[2] for x in message_lst]

print(f"The decrypted message is: {''.join(message_lst)}")
