key = int(input())
number_of_lines = int(input())
string = ""
for each_line in range(number_of_lines):
    current_letter = input()
    current_letter_as_number = ord(current_letter)
    decrypted_symbol = current_letter_as_number + key
    string += chr(decrypted_symbol)
print(string)