strings = input().split(', ')
new_list = strings

for string in strings:
    if string == '0':
        new_list.remove('0')
        new_list.extend('0')

print(list(map(int, new_list)))