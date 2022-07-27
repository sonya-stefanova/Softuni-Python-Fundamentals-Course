import re

valid_urls = []
pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
sentence = input()
while sentence:
    matches = re.search(pattern, sentence)
    if matches:
        valid_urls.append(matches.group(0))
    sentence = input()
for valid_url in valid_urls:
    print(valid_url)

# 6.2


import re

valid_urls = []
pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
sentence = input()
while sentence:
    matches = re.finditer(pattern, sentence)
    for match in matches:
        valid_urls.append(match.group(1))
    sentence = input()
for valid_url in valid_urls:
    print(valid_url)
