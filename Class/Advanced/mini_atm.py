class ATM:
    def __init__(self):
        self.cash = 0

    def deposit(self, amount):
        self.cash += amount
        print(f"Добавихте {amount} лв. към наличността.")
        print(f"Нова наличност: {self.cash}")

    def withdraw(self, amount):
        if amount <= self.cash:
            self.cash -= amount
            print(f"Изтеглихте {amount} лв. от наличността.")
            print(f"Нова наличност: {self.cash}")
        else:
            print("Недостатъчна наличност!")
            print("Не можете да извършите транзакцията!")

    def info(self):
        print(f"Налични пари: {self.cash}")


atm = ATM()
while True:
    print("------------------")
    print("       MENU       ")
    print("------------------")
    print("1.Зареждане на банкомата")
    print("2.Теглене")
    print("3.Баланс")
    print("0.Изход")
    choice = int(input("Изберете своя избор: "))

    if choice == 1:
        amount = int(input("Въведете стойноста, която искате да добавите: "))
        atm.deposit(amount)

    elif choice == 2:
        amount = int(input("Въведете стойността, която искате да изтеглите: "))
        atm.withdraw(amount)

    elif choice == 3:
        atm.info()

    elif choice == 0:
        print("Довиждане!")
        break