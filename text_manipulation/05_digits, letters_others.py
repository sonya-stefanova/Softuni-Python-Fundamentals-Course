word = input()  #Agd#53Dfg^&4F53
nums = ""
letters = ""
others = ""

for symbol in word:
    if symbol.isdigit():
        nums += symbol
    elif symbol.isalpha():
        letters +=symbol
    else:
        others +=symbol
print(nums)
print(letters)
print(others)
