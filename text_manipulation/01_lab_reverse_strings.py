command = input()
new_word = ""
while command!= "end":
    new_word = command[::-1]
    print(f"{command} = {new_word}")
    command = input()
