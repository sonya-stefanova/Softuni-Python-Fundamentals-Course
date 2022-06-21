secret_message = input().split()

for word in secret_message:
    revealed = []

    numbers_in_message = [i for i in word if i.isdigit()]
    numbers_as_ascii = chr(int("".join(numbers_in_message)))
    revealed += numbers_as_ascii

    letters_in_message = [i for i in word if i.isalpha()]
    revealed += letters_in_message
    revealed[1], revealed[-1] = revealed[-1], revealed[1]
    print("".join(revealed), end=" ")