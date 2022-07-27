import re

furniture_names = []
total_cost = 0
data = input()

while not data == "Purchase":
    pattern = r"^>{2}(?P<name>[A-Za-z]+)<{2}(?P<price>\d+\.?\d+)!(?P<qty>\d+)$"

    furniture_data = re.match(pattern, data)
    if furniture_data:
        furniture_match = furniture_data.groupdict()
        furniture_names.append(furniture_match["name"])
        total_cost += float(furniture_match["price"]) * int(furniture_match["qty"])
    data = input()
print("Bought furniture:")

for furniture in furniture_names:
    print(furniture)

print(f"Total money spend: {total_cost:.2f}")