orders = int(input())
total = 0

for i in range(1, orders+1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price_each_order = ((days * capsules_count) * price_per_capsule)
    print(f"The price for the coffee is: ${price_each_order:.2f}")
    total+= price_each_order
print(f"Total: ${total:.2f}")