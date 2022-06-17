#first_solution:
# def smallest_of_three_numbers(num1, num2, num3):
#     smallest = min(num1, num2, num3)
#     return smallest
#
#
# number_one = int(input())
# number_two = int(input())
# number_three = int(input())
# print(smallest_of_three_numbers(number_one, number_two, number_three))

#second_solution:
def smallest_of_three_numbers(numbers_as_list: list):
    smallest = min(numbers_as_list)
    return smallest


number_one = int(input())
number_two = int(input())
number_three = int(input())
list_numbers = [number_one, number_two, number_three]
min_number_result = smallest_of_three_numbers(list_numbers)
print(min_number_result)