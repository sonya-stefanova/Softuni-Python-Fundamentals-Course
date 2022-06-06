numbers_str = input().split()
final_numbers = []

for num in numbers_str:
    final_numbers.append(int(num))

num_of_removals = int(input())

for _ in range(num_of_removals ):
    final_numbers.remove(min(final_numbers))

print(final_numbers)