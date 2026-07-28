try:
    first_number = float(input())
    second_number = float(input())
    result = first_number / second_number

except ValueError:
    print("Ошибка: введено не число")

except ZeroDivisionError:
    print("Ошибка: деление на ноль")

else:
    print(result)

finally:
    print("Завершение работы программы")
