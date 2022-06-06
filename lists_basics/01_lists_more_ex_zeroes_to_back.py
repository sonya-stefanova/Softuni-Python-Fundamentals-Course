list_of_numbers_as_string = input().split(", ")
counter = 0
string_as_numbers = []

for element in list_of_numbers_as_string:
    string_as_numbers.append(int(element))

for j in range(len(string_as_numbers)-1, -1, -1):
    zero = string_as_numbers[j]
    if zero == 0:
        counter +=1
        string_as_numbers.remove(zero)

for i in range(1,counter+1):
    string_as_numbers.append(0)

print(string_as_numbers)