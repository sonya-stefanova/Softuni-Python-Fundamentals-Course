numbers = input().split(' ')
step = int(input())
counted = []
idx = 0
while len(numbers) > 0:
    idx = (idx + step - 1) % len(numbers)
    counted.append(numbers.pop(idx))
print(str(counted))
print(str(counted).replace(' ', ''))