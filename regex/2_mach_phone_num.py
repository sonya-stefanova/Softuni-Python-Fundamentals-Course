import re

pattern = r'\+359 2 [0-9]{3} [0-9]{4}\b|\+359-2-[0-9]{3}-[0-9]{4}\b'
#patter1 = r'\+359([ -])2\1[0-9]{3}\1[0-9]{4}\b"
phones = input()
matches = re.findall(pattern, phones)
print(", ".join(matches))