from math import floor

companions = int(input())
days = int(input())
coins = 0

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    if current_day % 3 == 0:
        coins -= 3 * companions
    if current_day % 5 == 0:
        coins += 20 * companions
        if current_day % 3 == 0:
            coins -= 2 * companions
    coins += 50
    coins -= 2 * companions
coins_per_companions = coins/companions
print(f"{companions} companions received {floor(coins_per_companions)} coins each.")
