# numbers_as_digits = [int(x) for x in input().split(" ") if int(x) % 2 == 0]
# print(numbers_as_digits)
#
# numbers_as_digits = [int(x) for x in input().split(" ")]
# is_even = lambda x: x % 2==0
# result = filter(is_even, numbers_as_digits)
# print(list(result))


def is_even(num):
    if int(num) % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []
for current_number in numbers:
    if is_even(current_number):
        filtered_numbers.append(int(current_number))
print(filtered_numbers)
