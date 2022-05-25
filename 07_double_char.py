string = ""

while string != "End":
    string = input()

    if string == "SoftUni" or string == "End":
        continue

    for i in range(0, len(string)):
        print(f"{string[i]}{string[i]}", end="")
    print()

#second_variant
# string = input()
#
# while string != 'End':
#     new_string = ''
#
#     if string == 'SoftUni':
#         string = input()
#         continue
#     else:
#         for current_symbol in string:
#             new_string += current_symbol * 2
#         print(new_string)
#     string = input()

# third variant
# string = input()
# while string != "End":
#     if string != 'SoftUni':
#         for char in string:
#             print(char, end='')
#             print(char, end='')
#         print()
#     string = input()

#forth_variant
# word = input()
#
# while word != 'End':
#     new_word = ''
#
#     if word == 'SoftUni':
#         word = input()
#         continue
#     else:
#         for current_symbol in word:
#             new_word += current_symbol * 2
#         print(new_word)
#
#     word = input()