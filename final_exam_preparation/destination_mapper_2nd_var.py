import re

text = input()

pattern = r"(?<=(\=|/))(?P<destination>[A-Z][a-zA-Z]{2,})(?=\1)"

matches = [element.group("destination") for element in re.finditer(pattern, text)] #['Hawai', 'Cyprus']

travel_points = 0

for match in matches:
    travel_points += len(match)

print(f"Destinations: {', '.join(matches)}")
print(f"Travel Points: {travel_points}")