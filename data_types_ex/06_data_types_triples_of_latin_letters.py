#First Solution
number_of_characters = int(input())

starting_number = 97
for first_letter in range(starting_number, starting_number+number_of_characters):
    for second_letter in range(starting_number, starting_number+number_of_characters):
        for third_letter in range(starting_number, starting_number+number_of_characters):
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}")


#second solution:
# #number_of_characters = int(input())
#
# for first_letter in range(number_of_characters):
#     for second_letter in range(number_of_characters):
#         for third_letter in range(number_of_characters):
#             print(f"{chr(97+first_letter)}{chr(97+second_letter)}{chr(97+third_letter)}")

