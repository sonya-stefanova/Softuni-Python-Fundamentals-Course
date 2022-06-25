numbers = list(map(int, input().split(" ")))

average_sum = (sum(numbers) / len(numbers))
empty_list = []

filtered_numbers_greater_than_average = list(filter(lambda el: el > average_sum, numbers))

if 1 <= len(filtered_numbers_greater_than_average) < 5:
    print(*sorted(filtered_numbers_greater_than_average, reverse=True), sep=" ")

elif len(filtered_numbers_greater_than_average) >= 5:
    sorted_list = sorted(filtered_numbers_greater_than_average, reverse=True)
    del sorted_list[5:]
    print(*sorted_list, sep=" ")

else:
    print("No")