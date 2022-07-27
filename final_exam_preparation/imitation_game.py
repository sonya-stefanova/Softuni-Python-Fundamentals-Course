encrypted_msg = input()

while True:
    command = input()
    if command == "Decode":
        break

    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        first_letters = encrypted_msg[:number_of_letters]
        last_letters = encrypted_msg[number_of_letters:]
        
        encrypted_msg = first_letters + last_letters
        
    if action == "Insert":
        index = int(command[1])
        value = command[2]
        
        encrypted_msg = encrypted_msg[:index] + value + encrypted_msg[index:]
        
    if action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        
        if substring in encrypted_msg:
            encrypted_msg = encrypted_msg.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_msg}")