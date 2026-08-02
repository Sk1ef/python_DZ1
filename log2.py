num = int(input("Введите число от 1 до 5: "))
values = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
if num in values:
    print(values[num])
else:
    print("Ключ не найден")