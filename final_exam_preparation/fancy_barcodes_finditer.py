import re

number_products = int(input())

pattern = re.compile(r"@[#]+(?P<found_text>[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+")

for product_input in range(number_products):
    barcode = input()
    matches = re.finditer(pattern, barcode)
    found = False
    for match in matches:
        found = True
        result_print = ''.join(x for x in match["found_text"] if x.isdigit())
        if result_print:
            print(f"Product group: {result_print}")
        else:
            print(f"Product group: 00")
    if not found:
        print("Invalid barcode")