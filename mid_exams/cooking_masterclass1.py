from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
total_apron = 0
total_egg = 0
total_flour = 0

for student in range(1, students+1):
    if student == 0:
        print(f"{budget:.2f}$ more needed.")

    else:
        if student % 5 == 0:
            flour_sum = 0

        total_apron += ceil(apron_price*1.2)
        total_egg += egg_price*10
        total_flour += flour_price

total_sum = total_flour + total_egg + total_apron

if total_sum <= budget:
    print(f"Items purchased for {total_sum:.2f}$.")
else:
    needed_money = total_sum-budget
    print(f"{needed_money:.2f}$ more needed.")


