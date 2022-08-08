import re
pattern = r'([=/])(?P<destination>[A-Z][A-z]{2,})\1'
line = input()

matches = re.finditer(pattern, line)
result = [match_obj.group("destination") for match_obj in matches] #['Hawai', 'Cyprus']
print(f"Destinations: {', '.join(result)}")
travel_points = 0
for el in result:
    travel_points+=len(el)
print(f"Travel Points: {travel_points}")