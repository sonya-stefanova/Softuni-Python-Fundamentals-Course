encrypted_msg = input()

def move(msg, n):
    first_part_msg, left_msg = msg[:n], msg[n:]
    result = left_msg+first_part_msg
    return result

def insert(msg, i, val):
    msg_before, msg_after = msg[:i], msg[i:]
    result = msg_before+val+msg_after
    return result


def change_all(msg, sub_s, text):
    result = msg.replace(sub_s, text)
    return result


descrypted_message = ""
while True:
    command = input()
    if command == "Decode":
        break

    operations = command.split("|")
    action = operations[0]

    if action == "Move":
        num_chars = int(operations[1])
        descrypted_message = move(encrypted_msg, num_chars)

    elif action == "Insert":
        index = int(operations[1])
        value = operations[2]
        descrypted_message = insert(encrypted_msg, index, value)

    elif action == "ChangeAll":
        substring = operations[1]
        replacement_text = operations[2]

        descrypted_message = change_all(encrypted_msg, substring, replacement_text)

print(f"The decrypted message is: {descrypted_message}")