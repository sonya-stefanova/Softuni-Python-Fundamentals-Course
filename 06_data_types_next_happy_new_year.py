# year = int(input())
#
# is_happy_new_year = False
# current_year = year
#
# while not is_happy_new_year:
#     current_year += 1
#     unique = [int(digit) for digit in set(str(current_year))]
#     if len(unique) == len(str(current_year)):
#         print(current_year)
#         is_happy_new_year = True
#         break


# year = int(input())
#
# is_happy_new_year = False
# while not is_happy_new_year:
#     year+=1
#     set_year = set()
#
#     for i in range(len(str(year))):
#         set_year.add(str(year)[i])
#
#     is_happy_new_year = len(set_year)==len(str(year))
#
# print(year)



int_year = int(input())
unique_happy_new_year = False
while not unique_happy_new_year:
    int_year += 1
    str_year = str(int_year)
    if len(set(str_year)) == len(str_year):
        print(str_year)
        break
