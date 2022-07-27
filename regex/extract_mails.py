import re

line = input()
pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'  #r'\s(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
matches = re.findall(pattern, line)
for match in matches:
    print(match[0])

import re

# text = input()
# regex = r"((?<= )[a-z0-9]+)([\._-]?)([a-z0-9]*)@([a-z]+-?[a-z]*)(\.[a-z]+-?[a-z]*)+\b"
# matches = re.finditer(regex, text)
# res = [x.group(0) for x in matches]
# print(*res, sep='\n')