def social_distribution(nums: list, treshold: int):
    for index in range(len(nums)):
        if nums[index] < treshold:
            min_wealth_index = nums.index(min(nums))
            max_wealth_index = nums.index(max(nums))
            if nums[max_wealth_index] > nums[min_wealth_index]:
                difference = treshold - nums[min_wealth_index]
                nums[min_wealth_index] += difference
                nums[max_wealth_index] -= difference
    if min(nums) == treshold:
        return True, nums
    else:
        return False


population_list = list(map(int, input().split(', ')))
minimum_wealth = int(input())
if social_distribution(population_list, minimum_wealth):
    print(population_list)
else:
    print("No equal distribution possible")