text = input()

current_rage = ""
final_text = ""
i = 0
while i < len(text):
    if not text[i].isdigit():
        current_rage += text[i]
        i += 1
    else:
        number = ""
        while i < len(text) and text[i].isdigit():
            number += text[i]
            i += 1
        number = int(number)
        final_text += current_rage.upper() * number
        current_rage = ""

print(f"Unique symbols used: {len(set(final_text))}")
print(final_text)


# # 2-nd decision:
# def rage_quit(text):
#     new_text = ''
#     part = ''
#
#     for i in range(len(text)):
#         num = ''
#         if text[i].isdigit():
#             while i < len(text) and text[i].isdigit():
#                 num += text[i]
#                 i += 1
#             num = int(num)
#             new_text += part.upper() * num
#             part = ''
#             continue
#         if not text[i].isdigit():
#             part += text[i]
#
#     print(f'Unique symbols used: {len(set(new_text))}')
#     print(new_text)
#
#
# input_line = input()
# rage_quit(input_line)