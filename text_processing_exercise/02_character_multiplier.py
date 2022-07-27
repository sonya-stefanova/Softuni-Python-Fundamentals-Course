str1, str2 = input().split()
total = 0

str1 = [ord(i) for i in str1]
str2 = [ord(j) for j in str2]

is_shorter_or_equal = len(str1) if len(str1) <= len(str2) else len(str2)
is_longer = str1 if len(str1) > len(str2) else str2

for x in range(is_shorter_or_equal):
    total += str1.pop(0) * str2.pop(0)

if is_longer:
    total += sum(is_longer)

print(total)