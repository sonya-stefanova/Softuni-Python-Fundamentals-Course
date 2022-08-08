import re
pattern = r'(@#{1,})(?P<valid_text>[A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})'

num = int(input())

for i in range(num):
    command = input()
    matches = re.match(pattern, command)
    product_group = ''
    if matches:
        for char in matches.group('valid_text'):
            if char.isdigit():
                product_group+=char

        if product_group == "":
            print(f'Product group: 00')
        else:
            print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
