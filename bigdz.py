def calculate_average(grades):
    try:
        if not grades:
            return 0

        return sum(grades) / len(grades)
    except TypeError:
        print("Оценки должны быть числами")
        return 0


def calculate_total_average(students):
    if not students:
        return 0

    total = 0

    for student in students:
        total += calculate_average(student["grades"])

    return total / len(students)


def show_students(students):
    if not students:
        print("Список студентов пуст")
        return

    for student in students:
        average = calculate_average(student["grades"])

        if average >= 75:
            status = "Успешен"
        else:
            status = "Неуспешен"

        print(
            f"\nСтудент: {student['name']}\n"
            f"Оценки: {student['grades']}\n"
            f"Средний балл: {average:.2f}\n"
            f"Статус: {status}"
        )


def add_student(students, name, grades):
    try:
        if not grades:
            print("Нужно ввести хотя бы одну оценку")
            return

        grades = [int(grade) for grade in grades]

    except (ValueError, TypeError):
        print("Оценки должны быть списком чисел")
        return

    students.append({"name": name, "grades": grades})

    print(f'Студент "{name}" успешно добавлен.')

    total_average = calculate_total_average(students)
    print(f"Общий средний балл: {total_average:.2f}")


def add_student_from_input(students):
    name = input("Введите имя студента: ")

    grades_input = input(
        "Введите оценки через пробел: "
    )

    try:
        grades = [int(grade) for grade in grades_input.split()]
    except ValueError:
        print("Оценки должны быть числами")
        return

    add_student(students, name, grades)


def remove_worst_student(students):
    if not students:
        print("Список студентов пуст")
        return

    worst_student = students[0]
    worst_average = calculate_average(worst_student["grades"])

    for student in students:
        average = calculate_average(student["grades"])

        if average < worst_average:
            worst_student = student
            worst_average = average

    students.remove(worst_student)

    print(
        f'Студент с самым низким средним баллом '
        f'"{worst_student["name"]}" удалён.'
    )

    if students:
        total_average = calculate_total_average(students)
        print(f"Общий средний балл: {total_average:.2f}")
    else:
        print("Студентов больше нет")


def show_total_average(students):
    if not students:
        print("Список студентов пуст")
        return

    total_average = calculate_total_average(students)

    print(f"Общий средний балл: {total_average:.2f}")


def main(students):
    menu = {
        1: show_students,
        2: show_total_average,
        3: add_student_from_input,
        4: remove_worst_student
    }

    while True:
        print(
            "\n1. Показать всех студентов\n"
            "2. Показать общий средний балл\n"
            "3. Добавить студента\n"
            "4. Удалить студента с самым низким средним баллом\n"
            "5. Выход"
        )

        try:
            num = int(input("Введите номер операции от 1 до 5: "))
        except ValueError:
            print("Введено не число")
            continue

        if num == 5:
            print("Работа завершена")
            break

        if num in menu:
            menu[num](students)
        else:
            print("Неверный номер операции")


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

main(students)
