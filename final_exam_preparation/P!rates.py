command =input()
towns = {}
while command!="Sail":
    command =command.split("||")
    town, people, gold = command
    people = int(people)
    gold = int(gold)
    if town not in towns:
        towns[town] = {}
        towns[town]["people"] = people
        towns[town]["gold"] = gold

    else:
        towns[town]["people"] += people
        towns[town]["gold"] += gold

    command = input()

event_data = input()
while event_data!="End":
    split_event_data = event_data.split("=>")
    action = split_event_data[0]
    town=split_event_data[1]

    if action == "Plunder":
        people = int(split_event_data[2])
        gold = int(split_event_data[3])

        towns[town]["people"]-=people
        towns[town]["gold"]-=gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if towns[town]["people"] == 0 or towns[town]["gold"]==0:
            del towns[town]
            print(f"{town} has been wiped off the map!")


    elif action == "Prosper":
        gold = int(split_event_data[2])
        if gold>0:
            towns[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    event_data = input()

count = 0
count = len(towns)
if count > 0:
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
    for town, people_and_gold in towns.items():
        print(f"{town} -> Population: {people_and_gold['people']} citizens, Gold: {people_and_gold['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")