# string = input()
# dict = {}
# for char in string:
#     if char != " ":
#         if char not in dict:
#             dict[char] = 0
#         dict[char]+=1
#
# for char in dict:
#     print(f"{char} -> {dict[char]}")


# -----2nd variant------
letters = {}
symbols = ''.join(s for s in input().split())
print(symbols)
for letter in symbols:
    if letter not in letters.keys():  # not in letters
        letters[letter] = 0
    letters[letter] += 1
for key, value in letters.items():
    print(f"{key} -> {value}")

# for key in letters.keys():
#    print(f"{key} -> {letters[key]}")
