particles = input().split("|")
command = input()

while command != "Done":
    command_info = command.split(" ")
    current_command = " ".join(command_info[0:2])

    if current_command == "Move Left":
        index = int(command_info[2])
        if 0<= index-1<index <len(particles):
            particles[index],particles[index-1]= particles[index-1],particles[index]

    elif current_command == "Move Right":
        index = int(command_info[2])
        if 0<= index <index +1<len(particles):
            particles[index], particles[index+1] = particles[index+1], particles[index]

    elif current_command == "Check Even":
        even_position_elements = [particles[i] for i in range(len(particles)) if i%2 == 0]
        print(" ".join(even_position_elements))
    elif current_command == "Check Odd":
        odd_position_elements = [particles[i] for i in range(len(particles)) if i%2 != 0]
        print(" ".join(odd_position_elements))
    command = input()
print(f"You crafted {''.join(particles)}!")