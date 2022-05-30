starting_index = int(input())
finishing_index = int(input())
string = ""
for each_char in range(starting_index, finishing_index+1):
    string += chr(each_char) + " "
print(string)

