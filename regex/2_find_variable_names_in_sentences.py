import re
string = input()
pattern = r'(_)(?P<variable>[A-z0-9]+)'
variables = []
while string:
    matches = re.finditer(pattern, string)
    for match in matches:
        if match:
            variable = match.group("variable")
            variables.append(variable)
        else:
            continue
    string = input()
print(*variables, sep=",")