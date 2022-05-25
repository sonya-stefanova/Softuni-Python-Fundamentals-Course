divisor = int(input())
boundary = int(input())
max_multiplier = 0

#second_variant
# for current_number in range(boundary, divisor, -1):
#     if current_number % divisor == 0:
#         max_multiplier = current_number
#         break


for current_number in range(1, boundary+1):
    if current_number%divisor==0:
        max_multiplier=current_number
    if max_multiplier>current_number:
        break
print(max_multiplier)
