budget = int(input())
command = input()
is_enough_budget = True
while command != "End":
    product_price = int(command)

    budget -= product_price
    if budget < 0:
        is_enough_budget = False
        break

    command = input()

if is_enough_budget == True:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")