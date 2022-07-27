command = input().split(" ") #['hi', 'abc', 'add']
new_word = " "
for word in command:
    new_word+=word*len(word)
print(new_word)

# second variant ===>>> print(''.join(map(lambda x: x*len(x), input().split())))
