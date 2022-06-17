def multiplication_type(number1, number2, number3):
    multiplication_number_sequence = [number1, number2, number3]
    counter = 0
    for i in range(len(multiplication_number_sequence)):
        current_number = multiplication_number_sequence[i]
        if current_number < 0:
            counter +=1
        elif current_number == 0:
            return "zero"

    if counter % 2 != 0:
        return "negative"
    elif counter % 2 == 0:
        return "positive"





num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = multiplication_type(num_1, num_2, num_3)
print(result)
