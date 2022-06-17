import math
def calculate_factorial(number):
    if number == 0 or number ==1:
        return 1
    else:
        return number * math.factorial(number - 1)


first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_factorial(first_number)
second_number_factorial = calculate_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")