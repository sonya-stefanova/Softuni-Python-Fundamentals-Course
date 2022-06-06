n = int(input())
word = input()
list_of_words = []
filtered_list = []

for i in range (n):
    current_string = input()
    list_of_words.append(current_string)
print(list_of_words)

# for j in range(len(list_of_words)-1, -1, -1):
#     element = list_of_words[j]
#     if word not in element:
#         list_of_words.remove(element)
# print(list_of_words)

for j in range(len(list_of_words)):
    element = list_of_words[j]
    if word in element:
        filtered_list.append(element)
print(filtered_list)


