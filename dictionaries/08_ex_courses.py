command = input()
courses = {}

while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for course_name, list_of_student_names in courses.items():
    count_of_students = len(list_of_student_names)
    print(f"{course_name}: {count_of_students}")
    for current_student_name in list_of_student_names:
        print(f"-- {current_student_name}")