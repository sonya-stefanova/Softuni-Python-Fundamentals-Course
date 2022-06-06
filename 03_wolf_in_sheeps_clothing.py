animals = input().split(", ")

if animals[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
    (exit())
counter = -1
for wolf in range(len(animals) - 1, -1, -1):
    counter += 1
    if animals[wolf] == 'wolf':
        print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")