list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers: #string-ове
    opposite_numbers.append(-int(element))
print(opposite_numbers)