fires = input().split("#")
water = int(input())

total_efforts = 0
total_fire = 0
cells = []

print("Cells:")

for fire in fires:
    args = fire.split(" = ")
    fire_type = args[0]
    level = int(args[1])

    is_valid = False


    if water < level:
        continue

    if fire_type == 'High':
        if 81 <= level <= 125:
            is_valid = True
    elif fire_type == 'Medium':
        if 51 <= level <= 80:
            is_valid = True
    elif fire_type == 'Low':
        if 1 <= level <= 50:
            is_valid = True

    if is_valid:
        cells.append(level)
        water -= level
        total_efforts += level * 0.25
        total_fire += level


for cell in cells:
    print(f' - {cell}')

print(f'total_efforts: {total_efforts:.2f}')
print(f'Total Fire: {total_fire}')