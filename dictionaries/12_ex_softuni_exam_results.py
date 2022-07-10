command = input()
points_dict = {}
submissions_dict = {}


while command != "exam finished":
    split_command = command.split("-")

    if "banned" in command:
        username = split_command[0]
        banned = split_command[1]
        if username in points_dict:
            del points_dict[username]
    else:
        username = split_command[0]
        language = split_command[1]
        points = split_command[2]
        points = int(points)

        if username in points_dict:
            if points_dict[username] < points:
                points_dict[username] = points
        else:
            points_dict[username] = points

        if language not in submissions_dict:#правим изкуствен брояч с отделно дикшънъри
            submissions_dict[language] = 0
        submissions_dict[language] += 1
    command = input()


print("Results:")
for username, points in points_dict.items():
    print(f"{username} | {points}")
print("Submissions:")
for language, counter in submissions_dict.items():
    print(f"{language} - {counter}")

