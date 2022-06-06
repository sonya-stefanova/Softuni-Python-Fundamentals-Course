numbers_list = input().split(' ')
string = input()
message_list = []

for each_num in numbers_list:
    current_sum = 0
    for i in each_num:
        current_sum += int(i)
    #this is the index value

    current_sum %= len(string)

    message_list.append(string[current_sum])
    string = string.replace(string[current_sum], '', 1)

print(''.join(message_list))