import re

string = input()
calories_day = 0

expression = r'(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<exp_date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>[0-9]+)\1'

calories_matches = re.finditer(expression, string)
matches = re.finditer(expression, string)

for cal_match in calories_matches:
    if cal_match:
        calories = cal_match.group('calories')
        calories_day += int(calories)

print(f'You have food to last you for: {calories_day//2000} days!')

for match in matches:
    if match:
        item_name = match.group('item')
        exp_name = match.group('exp_date')
        cals = match.group('calories')
        print(f"Item: {item_name}, Best before: {exp_name}, Nutrition: {cals}")
