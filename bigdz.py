def calculate_average(grades):
    return sum(grades) / len(grades)


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
    students.append({"name": name, "grades": grades})

    print(f'Студент "{name}" успешно добавлен.')

    total_average = calculate_total_average(students)
    print(f"Общий средний балл: {total_average:.2f}")


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


students = [
    {"name": "Harry", "grades": [80, 90, 78]},
    {"name": "Hermione", "grades": [95, 90, 97]},
    {"name": "Ron", "grades": [60, 70, 64]},
    {"name": "Draco", "grades": [60, 75, 70]}
]


def main(students):
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

        if num == 1:
            show_students(students)

        elif num == 2:
            show_total_average(students)

        elif num == 3:
            name = input("Введите имя студента: ")

            grades_input = input(
                "Введите оценки через пробел: "
            )

            try:
                grades = [int(grade) for grade in grades_input.split()]
            except ValueError:
                print("Оценки должны быть числами")
                continue

            if not grades:
                print("Нужно ввести хотя бы одну оценку")
                continue

            add_student(students, name, grades)

        elif num == 4:
            remove_worst_student(students)

        elif num == 5:
            print("Работа завершена")
            break

        else:
            print("Неверный номер операции")


main(students)
