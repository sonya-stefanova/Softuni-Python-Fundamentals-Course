line = input().split()
bakery = {}

for i in range(0, len(line),2):
    key = line[i]
    value = line[i+1]
    bakery[key] = int(value)

print(bakery)


# ----------------- 2nd variant ------------------------------------------------------
# bakery_list = input().split(" ")
# bakery = {bakery_list[i]: int(bakery_list[i+1]) for i in range(0, len(bakery_list), 2)}
# print(bakery)