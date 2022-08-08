import re
furniture_list = []
total_cost = 0
data = input()

while not data == "Purchase":
    pattern = r"^>{2}(?P<name>[A-Za-z]+)<{2}(?P<price>\d+\.?\d+)!(?P<qty>\d+)$"
    matches = re.finditer(pattern, data)

    for match in matches:
        product_name = match.group('name')
        furniture_list.append(product_name)
        price = float(match.group('price'))
        quantity = int(match.group('qty'))
        total_cost +=quantity*price
    data = input()
print("Bought furniture:")

for furniture in furniture_list:
    print(furniture)

print(f"Total money spend: {total_cost:.2f}")