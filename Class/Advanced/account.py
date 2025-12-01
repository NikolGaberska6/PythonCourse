class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Добавихте {amount} в сметката '{self.account_number}'.")
        print(f"Общата сума в сметката е: {self.balance}")

    def withdraw(self, amount, pin):
        if pin == self.pin:
            self.balance -= amount
            print(f"Изтеглихте {amount} от сметката '{self.account_number}'.")
            print(f"Сумата на сметката след тегленето е: {self.balance}")

    def get_info(self):
        print(f"Номера на сметката: {self.account_number} с баланс: {self.balance}")

account_number = input("Въведете номер на сметката: ")
balance = int(input("Въведете началния баланс: "))
pin = int(input("Въведете пин код: "))
active_account = Account(account_number, balance, pin) #инстанция на класа
print("================== МЕНЮ ==================")
print("1.Депозит\n" "2.Теглене\n" "3.Инфо за сметката" "4.Изход")
while True:
 option = int(input("Изберете опция: "))
 if option == 1:
    deposit = int(input("Въведете депозит: "))
    active_account.deposit(deposit)
 elif option == 2:
    withdraw_price = int(input("Въведете сума за теглене: "))
    pin = int(input("Въведете пин код: "))
    active_account.withdraw(withdraw_price, pin)
 elif option == 3:
    active_account.get_info()
 elif option == 4:
     break
