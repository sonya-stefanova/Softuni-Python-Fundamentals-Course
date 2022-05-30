lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
shield_counter = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        total_expenses += helmet_price
    if i % 3 == 0:
        total_expenses += sword_price
    if i % 2 == 0 and i % 3 == 0:
        total_expenses += shield_price
        shield_counter += 1
    if shield_counter == 2:
        total_expenses += armor_price
        shield_counter = 0

print(f"Gladiator expenses: {total_expenses:.2f} aureus")