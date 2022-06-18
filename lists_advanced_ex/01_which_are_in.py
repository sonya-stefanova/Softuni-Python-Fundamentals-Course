first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_sequence = []
for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word and not first_word in new_sequence:
            new_sequence.append(first_word)
print(new_sequence)


