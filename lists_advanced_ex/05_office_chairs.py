room_numbers = int(input())

count_free_chairs = 0
enough_chairs = True

for room in range(1, room_numbers + 1):
    data = input().split(' ')
    chairs_x = data[0]
    visitors = int(data[1])

    available_chairs = chairs_x.count("X")
    left_chair = abs(available_chairs - visitors)
    if available_chairs < visitors:
        print(f'{left_chair} more chairs needed in room {room}')
        enough_chairs = False
    else:
        count_free_chairs += left_chair

if enough_chairs:
    print(f'Game On, {count_free_chairs} free chairs left')