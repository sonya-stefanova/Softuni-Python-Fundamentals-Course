commands = input()
meals_collection = {}
unliked_meals = []

while commands != "Stop":
    splitted_commands = commands.split("-")
    action, guest, meal = splitted_commands

    if action == "Like":
        if guest not in meals_collection:
            meals_collection[guest] = []
        if meal not in meals_collection[guest]:
            meals_collection[guest].append(meal)

    elif action == "Unlike":
        if guest not in meals_collection.keys():
            print(f"{guest} is not at the party.")
        else:
            if meal not in meals_collection[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")

                unliked_meal = meals_collection.pop(guest)
                unliked_meals.append(unliked_meal)
    commands = input()
counter_unliked_meals= len(unliked_meals)
meals_collection = dict(sorted(meals_collection.items(), key=lambda u: (-len(u[1]), u[0])))
for guest, meal_list in meals_collection.items():
    print(f"{guest}: {', '.join(meal_list)}")
print(f"Unliked meals: {counter_unliked_meals}")

