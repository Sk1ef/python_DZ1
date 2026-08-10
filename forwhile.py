def sum_even_numbers():
    result = 0

    for i in range(2, 101, 2):
        result += i

    return result


def squares():
    return [x ** 2 for x in range(1, 11, 2)]


def count_user_input():
    count = 0
    number = 0

    while number >= 0:
        number = float(input("Введите число: "))
        count += 1

    return count


def main():
    print(f"Сумма чётных чисел от 1 до 100: {sum_even_numbers()}")
    print(f"Квадраты нечётных чисел от 1 до 10: {squares()}")
    print(f"Количество введенных чисел: {count_user_input()}")


main()