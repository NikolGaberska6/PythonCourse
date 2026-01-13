import sys
class Employee:
    def __init__(self, id, name, position, salary, experience):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.experience = experience

    def increase_salary(self):
        if self.experience > 5:
            print("Заплатата се увеличава с 10%!")
            plus = 0.1 * self.salary
            self.salary += plus
            print(f"Новата стойност на заплатата е: {self.salary} лв.")
        else:
            print("Недостатъчно опит!")
            print("Заплатата на работника не подлежи на увеличение!")

    def calculate_bonus(self):
        if self.experience > 10:
            bonus = 0.2 * self.salary
            print(f"Бонусът е 20% от заплатата - {bonus} лв.")
            self.salary += bonus
            print(f"Новата заплата с бонуса е равна на - {self.salary} лв.")
        elif 5 <= self.experience <= 10:
            bonus = 0.1 * self.salary
            print(f"Бонусът е 10% от заплатата - {bonus} лв.")
            self.salary += bonus
            print(f"Новата заплата с бонуса е равна на - {self.salary} лв.")
        else:
            print("Няма бонус!")
            print("Заплатата не подлежи на промяна!")

    def info(self):
        print(f"ID: {self.id}, Име: {self.name}, Позиция: {self.position}, "
              f"Заплата: {self.salary}, Години опит: {self.experience}.")

def search_by_position(employees, position):
    employee_of_given_position = []
    for employee in employees:
        if employee.position == position:
            employee_of_given_position.append(employee)

    if len(employee_of_given_position) > 0:
       print("Всички служители на дадената позиция: ")
       for employee in employee_of_given_position:
            print(employee.name)
    else:
        print("Няма служители на посочената позиция!")

def highest_salary(employees):
    max_salary = -sys.maxsize
    for employee in employees:
        if employee.salary > max_salary:
            max_salary = employee.salary
    if max_salary != -sys.maxsize:
        for employee in employees:
            if employee.salary == max_salary:
              print("Информацията за служителя с най-висока заплата: ")
              employee.info()
    else:
        print("Няма служител с най-висока заплата!")

def sort_by_experience(employees):
    employees.sort(key=lambda e: e.experience)
    print("Сортирахте служителите по години опит във възходящ ред!")
    print("Сортираният списък е: ")
    for employee in employees:
        employee.info()

def delete_low_salary(employees, min_salary):
    removed = False
    for employee in employees.copy():
        if employee.salary < min_salary:
            removed = True
            print(f"Изтрихте служителя {employee.name} от списъка със служители!")
            employees.remove(employee)
    if not removed:
        print("Няма служители с по-ниска заплата от посочената минимална!")
        print("Няма промяна в списъка!")

def main():
    employees = []
    n = int(input("Въведете броя на служителите, които искате да добавите в списъка: "))
    for i in range(n):
        id = input("Въведете ИД на служителя, който искате да добавите: ")
        name = input("Въведете име на служителя, който искате да добавите: ")
        position = input("Въведете позиция на служителя, който искате да добавите: ")
        salary = float(input("Въведете заплата на служителя, който искате да добавите: "))
        experience = int(input("Въведете години опит на служителя, който искате да добавите: "))
        employee = Employee(id, name, position, salary, experience)
        employees.append(employee)
        print("Успешно добавихте служителя в списъка със служители!")

    print("-------Проверка за увеличаване на заплатата на всеки служител---------")
    for employee in employees:
        print(f"Проверка на '{employee.name}'")
        employee.increase_salary()

    print("------- Изчисляване за бонус от заплатата на всеки служител---------")
    for employee in employees:
        print(f"Бонус на '{employee.name}'")
        employee.calculate_bonus()

    position = input("Въведете позицията, по която търсите: ")
    search_by_position(employees, position)

    highest_salary(employees)

    sort_by_experience(employees)

    min_salary = float(input("Въвдете минималната допустима заплата: "))
    delete_low_salary(employees, min_salary)

main()