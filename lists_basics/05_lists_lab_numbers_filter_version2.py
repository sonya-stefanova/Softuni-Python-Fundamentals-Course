n = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

numbers = []
filtered_number = []

for i in range(n):
    number = int(input())
    numbers.append(number)

command = input()

for num in numbers:
    filtered_command = (
        (command == COMMAND_EVEN and num %2 == 0) or
        (command == COMMAND_ODD and num %2 !=0) or
        (command == COMMAND_NEGATIVE and num < 0) or
        (command == COMMAND_POSITIVE and num >=0)
    )
    if filtered_command:
        filtered_number.append(num)
print(filtered_number)