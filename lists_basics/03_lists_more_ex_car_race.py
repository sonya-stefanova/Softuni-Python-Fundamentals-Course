numbers = input().split(' ')
half_numbers = len(numbers) // 2
left_player = numbers[:half_numbers]
right_player = numbers[-1:half_numbers:-1]
time_left_car = 0
time_right_car = 0

for each_period in left_player:
    time_left_car += int(each_period)
    if each_period == '0':
        time_left_car *=0.8

for current_time in right_player:
    time_right_car += int(current_time)
    if current_time == '0':
        time_right_car *=0.8

if time_left_car < time_right_car:
    print(f'The winner is left with total time: {time_left_car:.1f}')
else:
    print(f'The winner is right with total time: {time_right_car:.1f}')