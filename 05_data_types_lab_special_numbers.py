# number = int(input())
#
# for i in range(1, number + 1):
#     sum_of_digits = 0
#     digit = i
#
#     while digit > 0:
#         last_digit = digit%10
#         sum_of_digits += last_digit
#         digit = int(digit / 10)
#
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f"{i} -> True")
#     else:
#         print(f"{i} -> False")


# version 2 - Two FOR cycles
# number = int(input())
#
# for i in range(1, number + 1):
#     sum_of_digits = 0
#     digit = i
#
#     for digit in str(i):
#         sum_of_digits+=int(digit)
#
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f"{i} -> True")
#     else:
#         print(f"{i} -> False")


# version 3 - FOR & WHILE cycle
number = int(input())

for i in range(1, number + 1):
    sum_of_digits = 0
    digits = i

    while digits != 0:
        sum_of_digits += digits % 10
        digits = digits // 10

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
