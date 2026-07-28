while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: Введено не число")
        continue

    operation = input("Выберите операцию: +, -, /, *:\n")
    correct_operations = ["+", "-", "/", "*"]
    if operation not in correct_operations:
        print('Неизвестная операция')
        continue

    if operation == "+":
        print("Результат сложения: ", num1 + num2)
    elif operation == "-":
        print("Результат вычитания: ", num1 - num2)
    elif operation == "*":
        print("Результат умножения: ", num1 * num2)
    elif operation == "/":
        try:
            print("Результат деления: ", num1 / num2)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль")

    answer = input("Продолжить работу? (да/нет): ").lower()
    if answer != "да":
        print("Программа завершена.")
        break
