first_string = input()
second_string = input()
last_string = first_string

for symbol in range(len(first_string)):
    left = second_string[:symbol + 1]
    right = first_string[symbol + 1:]
    current_string = left + right
    if current_string == last_string:
        continue

    print(current_string)
    last_string=current_string
