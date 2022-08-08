import re

line = input()
numbers = []
while line:
    pattern = r'\d+'
    matches = re.findall(pattern, line)
    if matches:
        numbers.extend(matches)
    line = input()
print(*numbers, sep = " ")
