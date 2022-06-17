def loading_bar_function(integer):
    if integer == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{integer}% [{'%' * (integer // 10)}{'.' * (10 - integer // 10)}]\nStill loading..."

number = int(input())
print(loading_bar_function(number))