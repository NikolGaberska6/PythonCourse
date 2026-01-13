class BankAccount:
    def __init__(self, iban, owner, balance, type):
        self.iban = iban
        self.owner = owner
        self.balance = balance
        self.type = type

    def deposit(self, amount):
        print(f"Добавихте {amount} лв. към баланса на сметката!")
        self.balance += amount
        print(f"Новия баланс на сметката е: {self.balance} лв.")

    def withdraw(self, amount):
        if self.balance >= amount:
            print(f"Изтеглихте {amount} лв. от баланса на сметката!")
            self.balance -= amount
            print(f"Новия баланс на сметката е: {self.balance} лв.")
        else:
            print("Неуспешна транзакция!")
            print("Недостатъчно баланс по сметката!")

    def info(self):
        print(f"Айбан: {self.iban}, Собственик: {self.owner}, "
              f"Баланс: {self.balance}, Тип сметка: {self.type}.")

def search_by_owner(accounts, owner):
    account_by_owner = []
    for account in accounts:
        if account.owner == owner:
            account_by_owner.append(account)
    if len(account_by_owner) > 0:
        print("Всички сметки на дадения собственик: ")
        for account in account_by_owner:
            account.info()
    else:
        print("Няма собственик с посоченото име!")

def accounts_above_average(accounts):
    average_of_all_accounts = 0
    sum_of_all_accounts = 0
    for account in accounts:
       sum_of_all_accounts += account.balance

    if len(accounts) > 0:
        average_of_all_accounts = sum_of_all_accounts / len(accounts)
        print(f"Средния баланс на всички акаунти е: {average_of_all_accounts:.2f} лв.")
    else:
        print("Списъка с акаунти е празен!")

    account_with_above_average = []
    for account in accounts:
        if account.balance > average_of_all_accounts:
            account_with_above_average.append(account)
    if len(account_with_above_average) > 0:
        print("Списъка на сметките с баланс по-висок от средния: ")
        for account in account_with_above_average:
            account.info()
    else:
        print("Няма сметки в списъка с баланс по-висок от средния!")

    return account_with_above_average


def sort_by_balance(accounts):
    accounts.sort(key=lambda a: a.balance)
    print("Сортирахте сметките по баланс във възходящ ред!")
    print("Сортираният списък: ")
    for account in accounts:
        account.info()

def delete_empty_accounts(accounts):
    deleted_acc = 0
    for account in accounts.copy():
        if account.balance == 0:
            deleted_acc += 1
            print(f"Изтрихте акаунта с АЙБАН {account.iban} от списъка!")
            accounts.remove(account)
    if deleted_acc == 0:
       print("Няма акаунти с баланс равен на 0.00 в списъка с акаунти!")


def main():
    accounts = []
    n = int(input("Въведете колко броя банкови сметки искате да добавите: "))
    for i in range(n):
        iban = input("Въведете айбана на акаунта, който искате да добавите: ")
        owner = input("Въведете собственика на акаунта, който искате да добавите: ")
        balance = float(input("Въведете баланса на акаунта, който искате да добавите: "))
        type = input("Въведете типа на акаунта, който искате да добавите: ")
        account = BankAccount(iban, owner, balance, type)
        accounts.append(account)
        print("Успешно добавихте акаунта към списъка с акаунти!")

    found = False
    iban = input("Въведете айбана на акаунта, който искате да депозирате: ")
    for account in accounts:
        if account.iban == iban:
            found = True
            amount = float(input("Въведете сумата, която искате да депозирате: "))
            account.deposit(amount)
    if not found:
        print("Няма акаунт с посочения айбан в списъка с акаунти!")

    found = False
    iban = input("Въведете айбана на акаунта, от който искате да изтеглите : ")
    for account in accounts:
        if account.iban == iban:
           found = True
           amount = float(input("Въведете сумата, която искате да изтеглите: "))
           account.withdraw(amount)
    if not found:
        print("Няма акаунт с посочения айбан в списъка с акаунти!")


    owner = input("Въведете собственика на акаунта, който търсите: ")
    search_by_owner(accounts, owner)

    accounts_above_average(accounts)
    sort_by_balance(accounts)
    delete_empty_accounts(accounts)
    
main()