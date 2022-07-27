import re

line = input()
pattern = r"\d+"
all_nums = []

while line:
    numbers = re.findall(pattern, line)
    if numbers:
        all_nums.extend(numbers)

    line = input()

print(*all_nums)