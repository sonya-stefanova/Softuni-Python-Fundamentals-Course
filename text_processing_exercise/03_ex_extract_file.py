#C:\Internal\training-internal\Template.pptx
#C:\Projects\Data-Structures\LinkedList.cs

# path = input()
# splitted_path = path.split(".")
# extention = splitted_path[1]
# another_split = splitted_path[0].split("\\")
# file_name = another_split[-1]
#
#
# print(f"File name: {file_name}")
# print(f"File extension: {extention}")


path = input().split("\\")
filename, extension = path[-1].split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")