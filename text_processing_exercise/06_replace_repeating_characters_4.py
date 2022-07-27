data = input()

filtered_letters = ""
previous_letter = ""
for letter in data:
    if letter!=previous_letter:
        filtered_letters += letter
        previous_letter = letter
print(filtered_letters)
