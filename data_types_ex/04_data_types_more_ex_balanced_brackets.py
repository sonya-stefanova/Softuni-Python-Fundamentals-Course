number_of_lines = int(input())
is_balanced = False
closing_bracket = ")"
opening_bracket = "("
closing_bracket_counter = 0
opening_bracket_counter = 0
new_string = ""
for first_line in range(number_of_lines):
    char = input()
    new_string += char
    if "((" in new_string:
        is_balanced = False
        break
    if char == closing_bracket:
        closing_bracket_counter += 1
    elif char == opening_bracket:
        opening_bracket_counter += 1
        continue
if closing_bracket_counter == opening_bracket_counter:
    is_balanced = True

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
