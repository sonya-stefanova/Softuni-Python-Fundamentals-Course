happiness = input().split()
happiness_numbers = list(map(int, happiness))
factor = int(input())
happiness_multiplies = [each_num*factor for each_num in happiness_numbers]
average_happiness = sum(happiness_multiplies)/len(happiness_numbers)
all_happy_employees = [el for el in happiness_multiplies if el>=average_happiness]
happy_message = "Employees are happy!"
all_sad_employees = [el for el in happiness_multiplies if el<average_happiness]

sad_message = "Employees are not happy!"

if len(all_sad_employees)>len(happiness_multiplies)/2:
    print(f"Score: {len(all_happy_employees)}/{len(happiness_multiplies)}. {sad_message}")
else:
    print(f"Score: {len(all_happy_employees)}/{len(happiness_multiplies)}. {happy_message}")
