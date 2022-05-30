capacity = 255
water_counter = 0
number_of_lines = int(input())
insufficient_capacity = False
for line in range(number_of_lines):
    liters_of_water = int(input())
    if capacity - liters_of_water < 0:
       insufficient_capacity = True
       print("Insufficient capacity")
       continue
    water_counter+=liters_of_water
    capacity-=liters_of_water
print(water_counter)