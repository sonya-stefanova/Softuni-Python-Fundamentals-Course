def sum_of_char_code(first, second):
    total_sum = 0
    for i in range(len(first)):
        total_sum += ord(first[i]) * ord(second[i])
    for i in range(len(first), len(second)):
        total_sum += ord(second[i])
    return total_sum



two_string = input().split()
str1= two_string[0]
str2 = two_string[1]
if len(str1) > len(str2):
    print(sum_of_char_code(str2, str1))
else:
    print(sum_of_char_code(str1, str2))