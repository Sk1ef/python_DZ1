def sum_even_numbers():
    result = 0

    for i in range(2, 101, 2):
        result += i

    return result


def squares():
    return [x ** 2 for x in range(1, 11) if x % 2 != 0]


def count_user_input():
    count = 0
    number = float(input("Введите число: "))

    while number >= 0:
        count += 1
        number = float(input("Введите число: "))

    return count


def main():
    print(f"Сумма чётных чисел от 1 до 100: {sum_even_numbers()}")
    print(f"Квадраты нечётных чисел от 1 до 10: {squares()}")
    print(f"Количество введенных чисел: {count_user_input()}")


main()