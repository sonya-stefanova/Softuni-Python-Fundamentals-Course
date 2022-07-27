import re

main_string = input()

pattern = re.compile(r"([#|])(?P<item_name>[A-Za-z ]+)"
                     r"\1(?P<exp_date>[0-9]{2}/[0-9]{2}/[0-9]{2})"
                     r"\1(?P<calories>[0-9]{1,5})\1")
calories_last = 0
result_matches = []
result = re.finditer(pattern, main_string)

for show in result:
    calories_last += int(show["calories"])
    result_matches.append({"name": show["item_name"],
                        "expiration_date": show["exp_date"],
                        "calories": show["calories"]})

calories_last = int(calories_last / 2000)
print(f"You have food to last you for: {calories_last} days!")

for match in result_matches:
    print(f"Item: {match['name']}, Best before: {match['expiration_date']}, Nutrition: {match['calories']}")