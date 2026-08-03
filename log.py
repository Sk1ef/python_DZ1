def check(age, citizen, disqual):
    return age >= 18 and citizen.lower() == "да" and disqual.lower() == "нет"


try:
    age = int(input("Введите ваш возраст: "))
except ValueError:
    print("Возраст должен быть числом")
    exit()

citizen = input("Являетесь ли вы гражданином страны? (да/нет) ")
disqual = input("Имеются ли обстоятельства, не допускающие вас к выборам? (да/нет) ")

if check(age, citizen, disqual):
    print("Допущен")
else:
    print("Не допущен")
