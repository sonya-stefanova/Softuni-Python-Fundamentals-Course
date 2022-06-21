first_sequence = input().split(", ")
second_sequence = input()
new_sequence = [string for string in first_sequence if string in second_sequence]
print(new_sequence)