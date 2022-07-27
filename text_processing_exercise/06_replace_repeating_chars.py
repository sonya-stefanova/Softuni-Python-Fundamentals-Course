def replace_repeating_chars(chars):
    new_string = ''
    previous_char = ''
    for ch in chars:
        if previous_char == ch:
            pass
        elif previous_char != ch:
            new_string += ch
        previous_char = ch
    print(new_string)


chars = input()
replace_repeating_chars(chars)
