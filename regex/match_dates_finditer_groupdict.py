import re

text = input()

pattern = r"\b(?P<Day>\d{2})(?P<separator>(.|-|/))(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"
valid_dates = [match_obj.groupdict() for match_obj in re.finditer(pattern, text)]
print('\n'.join([f"Day: {date['Day']}, Month: {date['Month']}, Year: {date['Year']}" for date in valid_dates]))