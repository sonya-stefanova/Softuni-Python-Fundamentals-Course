integers = [int(number) for number in input().split(" ")]
average_sum = (sum(integers) / len(integers))
sorted_numbers = [num for num in sorted(integers, reverse=True) if num > average_sum]

if len(sorted_numbers) !=0:
    print(' '.join(map(str, sorted_numbers[:5])))
else:
    "No"
