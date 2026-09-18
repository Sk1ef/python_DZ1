def calculate_average(grades):
    try:
        if not grades:
            print("Список оценок пуст")
            return

        return sum(grades) / len(grades)

    except TypeError:
        print("Ошибка: оценки должны быть числами")
        return


def calculate_total_average(students):
    if not students:
        print("Список студентов пуст")
        return

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
    if not grades:
        print("Нужно ввести хотя бы одну оценку")
        return

    try:
        grades = [int(grade) for grade in grades]
    except (ValueError, TypeError):
        print("Ошибка: оценки должны быть списком чисел")
        return

    students.append({"name": name, "grades": grades})

    print(f'Студент "{name}" успешно добавлен.')

    total_average = calculate_total_average(students)
    print(f"Общий средний балл: {total_average:.2f}")


def add_student_from_input(students):
    name = input("Введите имя студента: ")
    grades_input = input("Введите оценки через пробел: ")

    try:
        grades = [int(grade) for grade in grades_input.split()]
    except ValueError:
        print("Ошибка: оценки должны быть числами")
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
        1: ("Показать всех студентов", show_students),
        2: ("Показать общий средний балл", show_total_average),
        3: ("Добавить студента", add_student_from_input),
        4: ("Удалить студента с самым низким средним баллом", remove_worst_student),
        5: ("Выход", None)
    }

    while True:
        for number in menu:
            print(f"{number}. {menu[number][0]}")

        try:
            num = int(input("Введите номер операции от 1 до 5: "))
        except ValueError:
            print("Введено не число")
            continue

        if num not in menu:
            print("Неверный номер операции")
            continue

        if num == 5:
            print("Работа завершена")
            break

        menu[num][1](students)


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]

main(students)