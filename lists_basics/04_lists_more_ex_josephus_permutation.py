initial_list_of_people = input().split(' ')
k = int(input())
executed_persons = []
people_count = len(initial_list_of_people) # we need to know how many people are there

index = 0
num = 1

while people_count > 0:
    new_list = [] #temporary variable where the remainder people will be saved

    for i, ch in enumerate(initial_list_of_people):
        person = initial_list_of_people[i]

        if num % k == 0:
            executed_persons.append(int(person))
        else:
            new_list.append(person)

        num += 1

    initial_list_of_people = new_list
    index = (index + 1) % people_count

print(str(executed_persons).replace(' ', ''))