number = int(input())

for i in range(number):
    current_num = int(input())
    if current_num <= 88:
        if current_num == 86:
            print("How are you?")
        elif current_num == 88:
            print("Hello")
        else:
            print("GREAT!")
    else:
        print("Bye.")