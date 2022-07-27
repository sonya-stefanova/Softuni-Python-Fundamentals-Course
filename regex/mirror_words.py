import re

line = input()

first_match = []
second_match = []
mirror_words = []

pattern = r"(?P<sep>[@#])(?P<match1>[A-Za-z]{3,})(?P=sep){2}(?P<match2>[A-Za-z]{3,})(?P=sep)"


matches = re.finditer(pattern, line)

for match in matches:
    first_match.append(match["match1"])
    second_match.append(match["match2"])

if len(first_match) == 0:
    print("No word matches found!")
else:
    print(f"{len(first_match)} word matches found!")

for el in range(len(first_match)):
    if first_match[el] == second_match[el][::-1]:
        mirror_words.append(first_match[el]+" <=> "+second_match[el])

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(f"{', '.join(mirror_words)}")