from math import ceil

num_students = int(input())
num_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
max_bonus_points = 0
max_student_attendences = ""

if num_lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for current_student in range (1, num_students+1):
        student_attendences = int(input())
        total_bonus = student_attendences / num_lectures * (5 + additional_bonus)
        if total_bonus>max_bonus_points:
            max_bonus_points = total_bonus
            max_student_attendences = student_attendences

    print(f"Max Bonus: {ceil(max_bonus_points)}.")
    print(f"The student has attended {ceil(max_student_attendences)} lectures.")
