def data_type(first_string: str, second_string: str):
    result = 0
    if first_string == 'int':
        result = int(second_string) * 2
    elif first_string == 'real':
        result = f'{float(second_string) * 1.5:.2f}'
    elif first_string == 'string':
        result = f"${second_string}$"
    return result


input_one = input()
input_two = input()
print(data_type(input_one, input_two))