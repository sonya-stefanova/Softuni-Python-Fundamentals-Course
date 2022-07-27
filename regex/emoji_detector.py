import re
line = input()
cool_treshold_calc = 1
cool_treshold_pattern = r'\d'
treshold_matches=re.findall(cool_treshold_pattern,line)
treshold_matches_int= [int(i) for i in treshold_matches]

for el in range(len(treshold_matches_int)):
    cool_treshold_calc*=treshold_matches_int[el]


print(f"Cool threshold: {cool_treshold_calc}")

emoji_pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1"
valid_emojis = re.finditer(emoji_pattern, line)
emojis = [obj.group() for obj in valid_emojis] #['::Smiley::', '**Tigers**', '::Mooning::', '**Shy**']

cool_emojis = []

for emoji in emojis:
    coolness = 0
    for char in emoji:
        if char.isalpha():
            coolness += ord(char)
    if coolness >= cool_treshold_calc:
        cool_emojis.append(emoji)

print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
