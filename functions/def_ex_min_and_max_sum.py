def min_number(nums:list):
    min_num = 0
    min_num = min(nums)
    return f"The minimum number is {min_num}"

def max_number(nums:list):
    max_num = 0
    max_num = max(nums)
    return f"The maximum number is {max_num}"

def sum_numbers(nums:list):
    total_sum = 0
    total_sum = sum(nums)
    return f"The sum number is: {total_sum}"


numbers = list(map(int,input().split()))
print(f"{min_number(numbers)}\n{max_number(numbers)}\n{sum_numbers(numbers)}")