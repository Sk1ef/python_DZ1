def summa():
    result = 0
    for i in range(1, 101):
        if i % 2 == 0:
            result += i
    return result


def squares():
    return [x ** 2 for x in range(1, 11) if x % 2 != 0]


def count_user_input():
    count = 0
    while True:
        number = float(input("Введите число: "))
        if number < 0:
            break
        count += 1
    return count


def main():
    print(f"Сумма чётных чисел от 1 до 100: {summa()}")
    print(f"Квадраты нечётных чисел от 1 до 10: {squares()}")
    print(f"Количество введенных неотрицательных чисел: {count_user_input()}")


main()