products_inventory = {}

while True:
    command = input()
    if command == 'statistics':
        break

    command = command.split(': ')
    product = command[0]
    quantity = int(command[1])

    if product not in products_inventory:
        products_inventory[product] = quantity
    else:
        products_inventory[product] += quantity

print('Products in stock:')
product_representation = [f'- {item}: {str(products_inventory[item])}' for item in products_inventory]
print('\n'.join(product_representation))
print(f'Total Products: {len(products_inventory)}')
print(f'Total Quantity: {sum(products_inventory.values())}')


#  ----more variants-----
# command = input()
# inventory = {}
# while command != "statistics":
#     product, quantity = command.split(": ")
#     quantity = int(quantity)
#     if product not in inventory:
#         inventory[product] = 0
#     inventory[product] += quantity
#     command = input()
#
# print("inventory in stock:")
# for product, quantity in inventory.items():
#     product_quantity_result = f"{product}: {quantity}"
#     print(product_quantity_result)
# print(f"Total inventory: {len(inventory.keys())}")
# print(f"Total Quantity: {sum(inventory.values())}")

# -----2nd version-----
# command = input()
# inventory = {}
# while command != "statistics":
#     product, quantity = command.split(": ")
#     quantity = int(quantity)
#     if product not in inventory:
#         inventory[product] = 0
#     inventory[product] += quantity
#     command = input()
#
# print("inventory in stock:")
# product_representation = [f'- {product}: {str(quantity)}' for product, quantity in inventory.items()]
# print('\n'.join(product_representation))
# print(f"Total inventory: {len(inventory.keys())}")
# print(f"Total Quantity: {sum(inventory.values())}")
