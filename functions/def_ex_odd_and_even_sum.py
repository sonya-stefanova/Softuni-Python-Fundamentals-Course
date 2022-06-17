def odd_and_even(nums: str):
    sum_odd = 0
    sum_even = 0
    for num in nums:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"
numbers = input()
current_numbers = list(map(int, str(numbers)))

result = odd_and_even(current_numbers)
print(result)

