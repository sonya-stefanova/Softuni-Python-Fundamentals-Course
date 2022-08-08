import re
pattern = r'([#@])(?P<word_one>[A-z]{3,})\1{2}(?P<word_two>[A-z]{3,})\1'
string = input()

matches = re.finditer(pattern, string)
pairs = re.finditer(pattern, string)

list_of_matches = [i.group() for i in matches]
mirror_words = []
for match in pairs:
    word_one = match.group("word_one")
    word_two = match.group("word_two")
    if match:
        if word_one == word_two[::-1]:
            mirror_words.append(f'{word_one} <=> {word_two}')

if len(list_of_matches)==0:
    print('No word pairs found!')
else:
    print(f'{len(list_of_matches)} word pairs found!')
if mirror_words:
    print(f'The mirror words are:\n{", ".join(mirror_words)}')
else:
    print("No mirror words!")