def count_num(num):
    if num < 0:
        print("Ошибка: Нужно ввести положительное число")
        return
    while num >= 0:
        print(num)
        num -= 1


try:
    num = int(input("Введите число: "))
except ValueError:
    print("Нужно ввести число")
    exit()

count_num(num)
