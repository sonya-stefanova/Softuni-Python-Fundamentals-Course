employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())

students_count = int(input())
help_per_hour = employee_1 + employee_2 + employee_3
hours = 0

while students_count > 0:
    hours += 1

    if hours % 4 == 0:
        continue

    students_count -= help_per_hour

print(f'Time needed: {hours}h.')