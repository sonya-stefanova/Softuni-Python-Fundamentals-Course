def palindrome_filter(word):
    if word == word[::-1]:
        return word

words = input().split(' ')
palindrome = input()

palindrome_list = [word for word in words if palindrome_filter(word)]
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')



words = input().split(' ')
palindrome = input()
palindromes = []
for word in words:
    if word == word[::-1]:
        palindromes.append(word)
print(palindromes)
print(f'Found palindrome {palindromes.count(palindrome)} times')