num_of_pairs = int(input())
students_dict = {}

for each_pair in range(num_of_pairs):
    student_name = input()
    grade = float(input())

    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(grade)

for student_name, list_of_grades in students_dict.items():
    average_grade = sum(list_of_grades)/len(list_of_grades)
    if average_grade>=4.50:
        print(f"{student_name} -> {average_grade:.2f}")