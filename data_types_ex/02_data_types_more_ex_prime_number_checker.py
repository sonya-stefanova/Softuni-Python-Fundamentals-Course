input_number = int(input())
number_is_prime = True
for i in range(2, input_number):
    if input_number % i == 0:
        number_is_prime = False
        break
if number_is_prime:
    print("True")
else:
    print("False")