password = input()
data = input()

while not data == "Done":
    data = data.split()
    command = data[0]

    if command == "TakeOdd":
        current_password = ""
        for i in range(len(password)):
            if i % 2 != 0:
                current_password += password[i]
        password = current_password
        print(password)

    elif command == "Cut":
        index = int(data[1])
        length = int(data[2])
        substring = password[index:index+length]
        password = password.replace(substring,'',1)
        print(password)

    elif command == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f"Nothing to replace!")

    data = input()
print(f"Your password is: {password}")
