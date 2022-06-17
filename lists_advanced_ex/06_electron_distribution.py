number_of_electrons = int(input())
new_list = list()
index = 1
while number_of_electrons > 0:
    max_value = 2*(index**2)
    if max_value > number_of_electrons:
        new_list.append(number_of_electrons)
    else:
        new_list.append(max_value)
    number_of_electrons -= max_value
    index += 1

print(new_list)