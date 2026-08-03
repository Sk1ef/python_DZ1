num = int(input("Введите число: "))

def count_num(num):
    assert num > 0, "Ошибка: Нужно ввести положительное число"
    while num >= 0:
        print(num)
        num -= 1

count_num(num)