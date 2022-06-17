letters = input()
counter = int(input())
# --first_variant--
# def repeat_string(letter, n):
#     result = letter *n
#     return result
# --second_variant--
repeat_string = lambda string, n: string*n
result = repeat_string(letters, counter)
print(repeat_string(letters, counter))