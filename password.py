cur_password = "qwerty123"
password = ""

while cur_password != password:
    password = input("Введите пароль: ")
    if cur_password == password:
        print("Пароль верный")
        break
    else:
        print("Пароль не верный")
