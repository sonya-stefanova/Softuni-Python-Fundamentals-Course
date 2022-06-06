numbers = input().split(' ')
string = input()
message = ''
string_list = list(string)

for chars in numbers:
    sum_of_numbers = 0

    for i in chars:
        sum_of_numbers += int(i)
        if sum_of_numbers > len(string):
            sum_of_numbers -= len(string)

    message += string_list[sum_of_numbers]
    string_list.pop(sum_of_numbers)

print(message)