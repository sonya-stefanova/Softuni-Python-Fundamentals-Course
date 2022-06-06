n = int(input())
word = input()
list_of_words = []
filtered_list = []

for i in range (n):
    current_string = input()
    list_of_words.append(current_string)
    if word in current_string:
        filtered_list.append(current_string)
print(list_of_words)
print(filtered_list)
