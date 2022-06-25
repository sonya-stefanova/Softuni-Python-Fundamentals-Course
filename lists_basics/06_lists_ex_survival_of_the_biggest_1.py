
integers = [int(number) for number in input().split(" ")]
count_num = int(input())

for num in range(count_num):
    min_number = integers[0]
    for i in range(len(integers)):
        if integers[i] < min_number:
            min_number = integers[i]
    integers.remove(min_number)
print(*integers, sep=', ')
