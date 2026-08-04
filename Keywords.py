def max_number(a, b):
    try:
        if a >= b:
            return a
        else:
            return b
    except TypeError:
        print("Невозможно сравнить")
        exit()


def empty_function():
    pass


def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def auto_test():
    assert max_number(5, 3) == 5, "Error"
    assert max_number(10, 10) == 10, "Error"
    assert max_number(3, 2) == 3, "Error"
    assert max_number(4, 8) == 8, "Error"
    print("Все тесты пройдены", "\n")


auto_test()
for num in even_numbers(10):
    print(num)
