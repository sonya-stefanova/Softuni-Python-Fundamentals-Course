str1, str2 = input().split(" ")
ord1 = [ord(char) for char in str1]
ord2 = [ord(char) for char in str2]
total_sum = 0

#calculating how many indeces we need to add:
if len(ord1) != len(ord2):
    needed_indices = abs(len(ord1)-len(ord2))

#cases with less or more symbols in the string:
if len(ord1) > len(ord2):
    for _ in range(needed_indices):
        ord2.append(1)
elif len(ord1) < len(ord2):
    for _ in range(needed_indices):
        ord1.append(1)

#calculating the total sum when lists are with equal length:
for i in range(len(ord1)):
    total_sum += ord1[i] * ord2[i]

print(total_sum)