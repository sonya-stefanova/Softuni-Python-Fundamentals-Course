command = input()
miner_dict = {}

while command != "stop":
    resource = command
    quantity = int(input())

    if resource not in miner_dict:
        miner_dict[resource] = 0
    miner_dict[resource]+=quantity

    command = input()

for resource, quantity in miner_dict.items():
    print(f"{resource} -> {quantity}")

