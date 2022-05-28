num = int(input())
sum = 0

for i in range(1, num + 1):
    i_str = str(i)

    while num>0:
        sum += int(i)

    if sum == 5 or sum == 7 or sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
