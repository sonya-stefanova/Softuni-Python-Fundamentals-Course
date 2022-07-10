course = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    action = command[0]

    if action == "Add":
        lesson_title = command[1]
        course.append(lesson_title)
    elif action == "Insert":
        lesson_title = command[1]
        index = int(command[2])
        if lesson_title not in course:
            course.insert(index, lesson_title)
            
    elif action == "Remove":
        lesson_title = command[1]
        if lesson_title in course:
            course.remove(lesson_title)
            if f'{lesson_title}-Exercise' in course:
                course.remove(f'{lesson_title}-Exercise')

    elif action == "Swap":
        first_lesson = command[1]
        second_lesson = command[2]
        if first_lesson in course and second_lesson in course:
            idx_1 = course.index(first_lesson)
            idx_2 = course.index(second_lesson)
            course[idx_1], course[idx_2] = course[idx_2], course[idx_1]

            if f'{first_lesson}-Exercise' in course:
                course.remove(f'{first_lesson}-Exercise')
                course.insert(idx_2 + 1, f'{first_lesson}-Exercise')
            elif f'{second_lesson}-Exercise' in course:
                course.remove(f'{second_lesson}-Exercise')
                course.insert(idx_1 + 1, f'{second_lesson}-Exercise')

    elif action == "Exercise":
        lesson_title = command[1]
        if lesson_title in course and "Exercise" not in lesson_title:
            idx = course.index(lesson_title)
            course.insert((idx+1), f"{lesson_title}-Exercise")
        elif lesson_title not in course:
            course.append(lesson_title)
            course.append(f"{lesson_title}-Exercise")

    command = input()
for index, course_title in enumerate(course, 1):
    print(f"{index}.{course_title}")
