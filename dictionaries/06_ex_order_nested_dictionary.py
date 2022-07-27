data = input()
orders_dict = {}

while data != "buy":
    split_data = data.split(" ")
    product = split_data[0]
    price = float(split_data[1])
    quantity = int(split_data[2])

    if product not in orders_dict:
        orders_dict[product] = {price, quantity}
    else:
        if orders_dict[product][0] != price:
            orders_dict[product][0] = price
        orders_dict[product][1] += quantity

    data = input()

for product in orders_dict:
    total_price = ..............
    print(f"{product} -> {total_price:.2f}")