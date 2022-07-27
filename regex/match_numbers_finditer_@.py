import re

text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = [match_object.group() for match_object in re.finditer(pattern, text)]

print(*matches)
