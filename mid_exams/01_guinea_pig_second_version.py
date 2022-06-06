quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
period = 30
weight = float(input()) * 1000
is_enough = True
for current_day in range(1, period + 1):
    quantity_food -= 300
    if current_day % 2 == 0:
        quantity_hay -= (0.05 * quantity_food)
    if current_day % 3 == 0:
        quantity_cover -= (1 / 3 * weight)
if quantity_cover >0 and quantity_hay>0 and quantity_food>0:
    is_enough = True
else:
    is_enough = False
if is_enough:
    print(f"Everything is fine! Puppy is happy! Food: {(quantity_food/1000):.2f}, Hay: {(quantity_hay/1000):.2f}, Cover: {(quantity_cover/1000):.2f}.")
else:
    print("Merry must go to the pet store!")