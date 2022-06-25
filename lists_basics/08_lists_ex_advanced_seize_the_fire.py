fires = input().split("#")
available_water = int(input())

total_efforts = 0
total_fire = 0
cells = []

print("Cells:")

for fire in fires:
    args = fire.split(" = ")
    fire_type = args[0]
    needed_water = int(args[1])

    is_valid = False


    if available_water < needed_water:
        continue

    if fire_type == 'High':
        if 81 <= needed_water <= 125:
            is_valid = True
    elif fire_type == 'Medium':
        if 51 <= needed_water <= 80:
            is_valid = True
    elif fire_type == 'Low':
        if 1 <= needed_water <= 50:
            is_valid = True

    if is_valid:
        cells.append(needed_water)
        available_water -= needed_water
        total_efforts += needed_water * 0.25
        total_fire += needed_water


for cell in cells:
    print(f' - {cell}')

print(f'total_efforts: {total_efforts:.2f}')
print(f'Total Fire: {total_fire}')