import re
string = input()
pattern = r"(?<=\s_)(?P<variable>[A-Za-z0-9]+)\b"

variables = []
while string:
    matches = re.finditer(pattern, string)
    for match in matches:
        variable_value = match.group("variable")
        variables.append(variable_value)
    string = input()
print(*variables, sep=",")