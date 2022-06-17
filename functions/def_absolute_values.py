# numbers = input().split(" ")
# abs_numbers = []
# for num in numbers:
#     absolute_number = abs(float(num))
#     abs_numbers.append(absolute_number)
# print(abs_numbers)

# numbers = map(float, input().split(" "))
# result = [abs(num) for num in numbers]
# print(result)


def absolute_numbers(nums):
    result = [abs(num) for num in nums]
    return result
numbers = list(map(float, input().split(" ")))
print(absolute_numbers(numbers))