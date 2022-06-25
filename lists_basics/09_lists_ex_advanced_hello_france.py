train_ticket = 150
# {type->price|type->price|type->price……|type->price}
# {budget}

list_of_items = input().split("|")
budget = float(input())
enough_money = False
list_of_prices = []
new_prices = []

for items in list_of_items:
    args = items.split("->")
    item_type = args[0]
    price = int(args[1])
    is_valid = False

    if item_type == 'Clothes':
        if price <= 50.00:
            is_valid = True
    elif item_type == 'Shoes':
        if price <= 35.00:
            is_valid = True
    elif item_type == 'Accessories':
        if price <= 20.50:
            is_valid = True

    if is_valid:
        if budget > price:
            budget -= price
            list_of_prices.append(price)
            new_prices.append(price * 1.4)

for new_price in new_prices:
    print(f'{new_price:.2f}', end=' ')
print('')

profit = sum(new_prices) - sum(list_of_prices)
print(f'Profit: {profit:.2f}')

new_budget = budget + sum(new_prices)
if new_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
