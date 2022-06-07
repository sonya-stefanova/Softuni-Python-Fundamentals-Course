command = input()
total_price = 0

while command != 'special' and command != 'regular':
    current_price = float(command)
    if current_price <= 0:
        print('Invalid price!')
    else:
        total_price += current_price
    command = input()

if total_price > 0:
    tax = total_price * 0.2

    if command == "regular":
        final_price_regular = tax + total_price

        print(f"Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {total_price:.2f}$')
        print(f'Taxes: {tax:.2f}$')
        print(f'-----------')
        print(f"Total price: {final_price_regular:.2f}$")

    elif command == 'special':
        final_price_special = (tax + total_price)*0.9
        print(f"Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {total_price:.2f}$')
        print(f'Taxes: {tax:.2f}$')
        print(f'-----------')
        print(f"Total price: {final_price_special:.2f}$")

else:
    print(f'Invalid order!')