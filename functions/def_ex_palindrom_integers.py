def is_palindrom_check(nums: list):
    for num in nums:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(', ')
is_palindrom_check(numbers)