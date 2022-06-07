#The Lift - MidExam
people_on_queue = int(input())

lift = list(map(int, input().split(' ')))

for i in range(len(lift)):
    can_load = min(4 - lift[i], people_on_queue)
    lift[i] += can_load
    people_on_queue -= can_load

if people_on_queue > 0 and i >= len(list):
    print(f"There isn't enough space! {people_on_queue} people in a queue!")
elif len([wagon for wagon in lift if wagon < 4]) > 0:
    print("The lift has empty spots!")

print(" ".join([str(wagon) for wagon in lift]))