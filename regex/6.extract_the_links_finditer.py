import re
string = input()

while string:
    regex = r"(w{3}\.)([a-zA-Z0-9]+[a-zA-Z0-9\-]+?[a-zA-Z0-9]+?\b)(\.[a-z]+)+"
    links = re.finditer(regex, string)
    for link in links:
        if link:
            print(link.group())
    string = input()