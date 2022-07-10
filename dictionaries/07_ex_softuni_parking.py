n = int(input())
command = input()
dict = {}

for i in range(n):
    command = input().split()
    username = command[1]

    if "register" in command:
        license_plate_number = command[2]
        if username not in dict:
            dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif "unregister" in command:
        if username in dict:
            dict.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate_number in dict.items():
    print(f"{username} => {license_plate_number}")

