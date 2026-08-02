try:
    age = int(input("Введите ваш возраст: "))
except ValueError:
    print("Возраст должен быть числом")
    exit()

citizen = input("Являетесь ли вы гражданином страны? (да/нет) ")
disqual = input("Имеются ли обстоятельства, не допускающие вас к выборам? (да/нет) ")

def check_age(age):
    if age >= 18:
         return True
    else:
        return False

def check_citizen(citizen):
    citizen = citizen.lower()
    if citizen == "да":
        return True
    else:
        return False

def check_disqual(disqual):
    disqual = disqual.lower()
    if disqual == "да":
        return False
    else:
        return True

if check_citizen(citizen) and check_age(age) and check_disqual(disqual) == True:
    print("Допущен")
else:
    print("Не допущен")