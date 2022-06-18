secret_message = input().split()

for word in secret_message:
    revealed_message = []

    numbers_in_message = [i for i in word if i.isdigit()]
    numbers_as_ascii = chr(int("".join(numbers_in_message)))
    revealed_message += numbers_as_ascii

    letters_in_message = [i for i in word if i.isalpha()]
    revealed_message += letters_in_message
    revealed_message[1], revealed_message[-1] = revealed_message[-1], revealed_message[1]
    print("".join(revealed_message), end=" ")