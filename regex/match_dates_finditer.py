import re

text = input()
expression = r"(?P<day>\d{2})(?P<sep>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"

matching_pattern = re.finditer(expression, text)

for match in matching_pattern:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')

    print(f'Day: {day}, Month: {month}, Year: {year}')
