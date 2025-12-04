class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def change_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
            print(f"Променихте заплата на {self.name} на {new_salary}")

    def info(self):
        print(f"Име: {self.name}, "
              f"Позиция: {self.position}, "
              f"Заплата: {self.salary}")

employees = []

while True:
    print("------------------------------")
    print("              МЕНЮ            ")
    print("------------------------------")

    print("1.Добавяне на служител")
    print("2.Промяна на заплата")
    print("3.Показване информация за служител")
    print("4.Всички служители")
    print("0.Изход")
    choice = int(input("Изберете опция: "))

    if choice == 1:
        name = input("Въведете името на служителя: ")
        position = input("Въведете позицията на служителя: ")
        salary = int(input("Въведете заплатата на служителя: "))
        emp = Employee(name, position, salary)
        employees.append(emp)

    elif choice == 2:
        name = input("Въведете името на служителя, чията заплата искате да промените: ")
        new_salary = int(input("Въведете новата заплата: "))
        for e in employees:
            if e.name == name:
                e.change_salary(new_salary)

    elif choice == 3:
        name = input("Въведете име на служител, чиято информация искате да принтирате: ")
        for e in employees:
            if e.name == name:
                e.info()

    elif choice == 4:
        for e in employees:
            e.info()

    elif choice == 0:
        print("Довиждане")
        break



