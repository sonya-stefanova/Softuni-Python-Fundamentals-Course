numbers = list(map(int, input().split(' ')))
average_number = sum(numbers) / len(numbers)
greater_then_aver_numbers = []

for number in numbers:
    if number > average_number:
        greater_then_aver_numbers.append(number)

#descending sort:
greater_then_aver_numbers.sort(reverse=True)
result = ' '.join(list(map(str, greater_then_aver_numbers[:5])))
if result:
    print(result)
else:
    print('No')