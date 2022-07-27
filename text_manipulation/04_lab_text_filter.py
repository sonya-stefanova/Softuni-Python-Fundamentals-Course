banned_words = input().split(", ")
piece_of_text = input()

for word in banned_words:
    while word in piece_of_text:
        piece_of_text = piece_of_text.replace(word, "*"*len(word))
print(piece_of_text)