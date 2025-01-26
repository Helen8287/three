#Определите класс "Account", имитируюий банковский счет.
#Класс должен включать атрибуты для хранения идентификатора владельца
#банкоского счета, методы для депозита(пополнения) и снятия средств,
#если на счету достаточно средств
#проверка баланса перед снятием денег, изменение и отслеживание состояния
#объекта


class Account():
    def  __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счете - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счёте")

        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = Account("id: 12332135", 600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)
