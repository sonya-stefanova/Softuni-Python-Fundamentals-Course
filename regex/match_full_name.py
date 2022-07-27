import re
names = input()

search_pattern = r'\b([A-Z][a-z]{2,} [A-Z][a-z]{2,})\b'
valid_names = re.findall(search_pattern, names)
print(" ".join(valid_names))