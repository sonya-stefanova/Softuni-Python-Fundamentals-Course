import re
line = input()
pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
matched_patterns_list = []

while line:
    matches = re.search(pattern, line)
    if matches:
        matched_patterns_list.append(matches)

    line = input()
for element in matched_patterns_list:
    print(element[0])

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