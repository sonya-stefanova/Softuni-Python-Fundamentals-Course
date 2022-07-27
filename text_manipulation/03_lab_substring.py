substring = input()
string_of_letters = input()

while substring in string_of_letters:
    string_of_letters = string_of_letters.replace(substring, "")
print(string_of_letters)