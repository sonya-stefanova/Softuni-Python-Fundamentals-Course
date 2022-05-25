number_of_orders = int(input())
total_price = 0
valid_order = True

for each_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule >100:
        valid_order = False
        continue
    elif days < 1 or days > 31:
        valid_order = False
        continue
    elif capsules_per_day > 2000 or capsules_per_day < 1:
        valid_order = False
        continue

    current_order_price = capsules_per_day * price_per_capsule * days
    total_price += current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")

print(f"Total: ${total_price:.2f}")
