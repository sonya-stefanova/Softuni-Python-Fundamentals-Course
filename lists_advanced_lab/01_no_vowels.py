word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_word = [current_letter for current_letter in word if current_letter not in vowels]
print("".join(new_word))