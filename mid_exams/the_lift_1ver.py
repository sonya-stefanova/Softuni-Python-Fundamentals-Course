people_waiting = int(input())
all_seats_on_lift = list(map(int, input().split(' ')))
new_list = list()

for wagon in range(len(all_seats_on_lift)):
    value_wagon = all_seats_on_lift[wagon]
    index =
    while people_waiting > 0:
        max_people_wagon = 4
        new_list.append(abs(max_people_wagon - value_wagon))

        people_waiting -= max_people_wagon
        index += 1

final_list = " ".join([str(wagon) for wagon in new_list])
if any(all_seats_on_lift) != max_people_wagon:
    print(f"The lift has empty spots!\n{final_list}")
else:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
