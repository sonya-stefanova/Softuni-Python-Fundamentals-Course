line = input().split()
products = input().split()
bakery = {}

for i in range(0, len(line),2):
    key = line[i]
    value = line[i+1]
    bakery[key] = int(value)

for product in products:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

# ---------second variant----------------------
# bakery_list = input().split(" ")
# bakery_dict = {bakery_list[item]: int(bakery_list[item+1]) for item in range(0, len(bakery_list), 2)}
# searched_products_list = input().split(" ")
#
# for product in searched_products_list:
#     if product in bakery_dict.keys():
#         print(f"We have {bakery_dict[product]} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")
