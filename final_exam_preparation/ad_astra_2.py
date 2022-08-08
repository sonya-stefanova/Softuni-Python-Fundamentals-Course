import re

line = input()
pattern = r'([#|])(?P<item>[A-Za-z\s]+)\1(?P<exp_date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>[0-9]+)\1'
total_cals = 0
needed_cals = 2000

matches = re.finditer(pattern, line)
result = [int(match_obj.group("calories")) for match_obj in matches]
total_cals = sum(result)
days_survival = int(total_cals/needed_cals)
print(f"You have food to last you for: {days_survival} days!")
for match in matches:
    item = match.group("item")
    expiration_date = match.group("exp_date")
    cals = match.group("calories")
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {cals}")