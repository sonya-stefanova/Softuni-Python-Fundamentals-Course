
def tribonacci_sequence(n):
    tribonaci_list = [1]
    for i in range(1, n):
        if len(tribonaci_list) < 3:
            tribonaci_list.append(i)
        else:
            tribonaci_list.append(sum(tribonaci_list[-3:]))
    tribonaci_list_as_string = list(map(str, tribonaci_list))
    return ' '.join(tribonaci_list_as_string)

number = int(input())
print(tribonacci_sequence(number))