import re


text = input()
expression = r'(\d{2})([-\/.])([A-Z][a-z]{2})\2(\d{4})'
find_matches = re.findall(expression, text)

for match in find_matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")