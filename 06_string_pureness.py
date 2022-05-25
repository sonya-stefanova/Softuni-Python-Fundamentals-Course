number_of_words = int(input())
counter = 0

for i in range(number_of_words):
    word = input()
    is_pure = True

    for index in range(len(word)):
        if word[index] == ',' or word[index] == '.' or word[index] == '_':
            is_pure = False

    if is_pure == False:
        print(f'{word} is not pure!')
    else:
        print(f'{word} is pure.')