neighborhood = list(map(int, input().split('@')))

idx = 0
failed = 0
command = input()
success = True

while True:
    if command == 'Love!':
        print(f"Cupid's last position was {idx}.")
        break

    step = int(command.split(' ')[1])
    idx += step

    if neighborhood[idx] == 0:
        print("Place {idx} has Valentine's day.")
    else:
        neighborhood[idx] -= 2
        if neighborhood[idx] == 0:
            print(f"Place {idx} has Valentine's day.")
    if idx >= len(neighborhood):
        idx = 0
    command = input()

for idx in neighborhood:
    if idx != 0:
        failed += 1
        success = False

if success:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")
