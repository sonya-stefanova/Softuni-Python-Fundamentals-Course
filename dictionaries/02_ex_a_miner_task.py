all_points = {}
students_points = {}
command= input()
while command != 'no more time':

    username, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in all_points:
        all_points[contest] = {}

    if username not in all_points[contest]:
        all_points[contest][username] = points

        if username not in students_points:
            students_points[username] = points
        else:
            students_points[username] += points
    else:
        if all_points[contest][username] < points:
            all_points[contest][username] = points
            students_points[username] = points
    command = input()
for k, v in all_points.items():
    number = 1
    print(f'{k}: {len(v)} participants')
    sorted_all_points = dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
    for k2, v2 in sorted_all_points.items():
        print(f'{number}. {k2} <::> {v2}')
        number += 1
print('Individual standings:')
sorted_students_points = sorted(students_points.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
number = 1
for name, points in sorted_students_points:
    print(f'{number}. {name} -> {points}')
    number += 1
