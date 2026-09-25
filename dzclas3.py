class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
print(f"Баланс после пополнения: {account.get_balance()}")

account.withdraw(300)
print(f"Баланс после снятия: {account.get_balance()}")