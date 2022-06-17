string_of_numbers = input().split(", ")
numbers = [int(num) for num in string_of_numbers]
even_indeces = [el for el in range(len(numbers)) if numbers[el] % 2==0]
print(even_indeces)