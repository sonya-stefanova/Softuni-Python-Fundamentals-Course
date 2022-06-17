def characters_in_range(sym_1, sym_2):
    collected_characters = []
    
    for current_character in range(ord(sym_1) + 1, ord(sym_2)):
        collected_characters.append(chr(current_character))
    return collected_characters


first_char = input()
second_char = input()
result = characters_in_range(first_char, second_char)
print(' '.join(result))
