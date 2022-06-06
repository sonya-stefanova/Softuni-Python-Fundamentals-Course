food_kg = float(input())
hay_kg = float(input())
cover_kg = float(input())
weight_kg = float(input())
c 
#input in grams
food_gr = food_kg * 1000
hay_gr = hay_kg * 1000
cover_gr = cover_kg * 1000
weight_gr = weight_kg * 1000
is_run_out_of_food = False
month_days = 30


for day in range(1, month_days + 1):
    food_gr -= 300
    if food_gr <= 0:
        is_run_out_of_food = True

    if day % 2 == 0:
        hay_gr -= food_gr * (5 / 100)
        if hay_gr <= 0:
            is_run_out_of_food = True

    if day % 3 == 0:
        cover_gr -= weight_gr * 1 / 3
        if cover_gr <= 0:
            is_run_out_of_food = True

    if is_run_out_of_food:
        print('Merry must go to the pet store!')
        break

if not is_run_out_of_food:
    print('Everything is fine! Puppy is happy! ' \
          f'Food: {food_gr / 1000:.2f}, ' \
          f'Hay: {hay_gr / 1000:.2f}, ' \
          f'Cover: {cover_gr / 1000:.2f}.')