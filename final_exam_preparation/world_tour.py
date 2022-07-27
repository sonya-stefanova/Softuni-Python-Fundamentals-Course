stops = input()

data = input()

while not data == "Travel":
    data = data.split(":")
    command = data[0]

    if command == "Add Stop":
        index = int(data[1])
        string = data[2]

        if index <= (len(stops) - 1):
            stops = stops[:index] + string + stops[index:]
        print(stops)

    elif command == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])

        if start_index <= (len(stops) - 1) and end_index <= (len(stops) - 1):
            stops = stops[:start_index] + stops[end_index + 1:]

        print(stops)

    elif command == "Switch":
        old_string = data[1]
        new_string = data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    data = input()

print(f"Ready for world tour! Planned stops: {stops}")