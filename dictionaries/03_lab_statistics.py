command = input()
products = {}

while not command == "statistics":
    data_to_sort = command.split(": ")
    product, quantity = data_to_sort
    quantity = int(quantity)

    if product not in products:
        products[product] = 0
    products[product]+=quantity
    command = input()

print("Products in stock:")

[print(f"- {product}: {quantity}") for product, quantity in products.items()]

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
