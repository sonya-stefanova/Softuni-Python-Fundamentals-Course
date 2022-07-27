import re

text = input()
search_pattern = r"(?<=\s_)[A-Za-z0-9]+\b"

variables = [obj.group() for obj in re.finditer(search_pattern, text)]

print(*variables, sep=',')