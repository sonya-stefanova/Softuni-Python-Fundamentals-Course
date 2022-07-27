command = input()
resources = {}

while command!= "stop":
    name = command
    quantity = int(input())
    if name not in resources:
        resources[name] = 0
    resources[name]+=quantity

    command = input()
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")