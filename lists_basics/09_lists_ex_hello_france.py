string = input().split("|")
ticket_price = 150
budget = float(input())
bought_products_price = []
new_prices = []

for element in string:
    items_for_sale = element.split("->")
    product_for_sale = items_for_sale[0]
    price = float(items_for_sale[1])

    if product_for_sale == "Clothes":
        if price > 50.00:
            continue
    if product_for_sale == "Shoes":
        if price > 35.00:
            continue
    if product_for_sale == "Accessories":
        if price > 20.50:
            continue

    if budget < price:
        continue
    else:
        budget -= price
        bought_products_price.append(price)
        new_prices.append(price * 1.4)

for new_price in new_prices:
    print(f'{new_price:.2f}', end=' ')
print()
profit = sum(new_prices) - sum(bought_products_price)
print(f'Profit: {profit:.2f}')

new_budget = budget + sum(new_prices)
if ticket_price <= new_budget:
    print("Hello, France!")
else:
    print(f"Not enough money.")
