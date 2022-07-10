number_of_towns = int(input())

total_profit = 0

for each_town in range(1, number_of_towns + 1):
    curr_town = input()
    income = float(input())
    expenses = float(input())

    if each_town % 5 == 0:
        income = income - income * 0.1
        each_profit = income - expenses
        total_profit += each_profit

        print(f"In {curr_town} Burger Bus earned {each_profit:.2f} leva.")

    else:
        if each_town % 3 == 0:
            expenses += expenses * 0.5
            each_profit = income - expenses
            total_profit += each_profit

            print(f"In {curr_town} Burger Bus earned {each_profit:.2f} leva.")

        else:
            each_profit = income - expenses
            total_profit += each_profit

            print(f"In {curr_town} Burger Bus earned {each_profit:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")