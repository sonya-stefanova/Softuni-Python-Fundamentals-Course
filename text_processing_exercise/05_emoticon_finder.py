#There are so many emoticons nowadays :P. I have many
chars = input()
#
# next_chars = [chars[ch+1] for ch in range(len(chars)) if chars[ch].startswith(":")]
# for ch in next_chars:
#     print(f":{ch}")


emojis = [f"{chars[i]}{chars[i+1]}"for i in range(len(chars)) if chars[i].startswith(":")]
print('\n'.join(emojis))