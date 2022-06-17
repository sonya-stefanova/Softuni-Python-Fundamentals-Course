def odd_even_digits(num: str):
    even_sum = 0
    odd_sum = 0
    for char in num:
        digit = int(char)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
result = odd_even_digits(number)
print(result)
