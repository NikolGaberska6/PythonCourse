import sys
class BankAccount:
    def __init__(self, account_number, name, balance): #фунцията в класа се нарича метод
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, d):
        self.balance += d
        print(f"Вкарахте {d} лева в сметката!")

    def withdrawing_money(self, w):
        if self.balance < w:
            print("Неуспешна транзакция! Недостатъчно пари в сметката!")
        else:
            print(f"Изтеглихте {w} пари!")
            self.balance -= w

    def print_info(self):
        print(f"Номер на акаунт: {self.account_number}, Име: {self.name}, "
              f"Баланс: {self.balance}.")

account_list = []
for i in range(10):
    account_number = int(input("Въведете номера на акаунт: "))
    name = input("Въведете името на потребителя: ")
    balance = float(input("Въведете баланса по сметката:  "))
    account = BankAccount(account_number, name, balance)
    account_list.append(account)

def max_balance():
    # max_number = -sys.maxsize #-938953069493486
    # min_number = sys.maxsize #938953069493486
    max_balance_person = -sys.maxsize
    for person in account_list:
        if person.balance > max_balance_person: #-938953069493486
            max_balance_person = person.balance
    return max_balance_person

def sort_by_name():
#    account_list.sort(key=lambda a: a.name) #във възходящ ред
     account_list.sort(key=lambda a:a.name, reverse=True) #в низходящ ред - променя листа
#    sorted_list = sorted(account_list, key=lambda a:a.name, reverse=True) #в низходящ ред - в нов лист
     print("Сортирахте листа във възходящ ред")


found = False
account_number = int(input("Въведете номера на сметката, по която искате  да депозирате: "))
for person in account_list:
    if person.account_number == account_number:
        found = True
        d = float(input("Въведете сумата, която искате да депозирате: "))
        person.deposit(d)
if not found:
    print("Няма такъв номер на акаунт!")


found = False
account_number = int(input("Въведете номера на сметката, от която искате  да изтеглите: "))
for person in account_list:
    if person.account_number == account_number:
        found = True
        w = float(input("Въведете сумата, която искате да изтеглите: "))
        person.withdrawing_money(w)
if not found:
    print("Няма такъв номер на акаунт!")

found = False
account_number = int(input("Въведете номера на сметката, за която искате информацията: "))
for person in account_list:
     if person.account_number == account_number:
            person.print_info()
if not found:
    print("Няма такъв номер на акаунт!")

for account in  account_list:
    account.print_info()

max_balance()
sort_by_name()