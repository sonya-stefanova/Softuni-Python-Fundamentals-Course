import re
#dd{separator}MMM{separator}yyyy

pattern = r'(\d{2})([-\/.])([A-Z][a-z]{2})\2(\d{4})'
line = input()
matches = re.findall(pattern,line)
for match in matches:
    if match:
        print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')