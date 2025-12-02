class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        percent = percent/100
        self.salary += percent * self.salary
        print(f"Увеличена заплата с {percent} %")

    def info(self):
        print(f"{self.name}, {self.position}, {self.salary}")

    def is_manager(self):
        if self.position == "Manager":
            print(True)
        else:
            print(False)

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary(self):
        for emp in self.employees:
           all_sum =  sum(emp.salary)
        return all_sum

    def manager(self):
        print("Всички мениджъри: ")
        for emp in self.employees:
            if emp.position == "Manager":
                emp.info()

    def highest_salary(self):
        highest_salary_emp = self.employees[0]
        for emp in self.employees:
            if emp.salary > highest_salary_emp.salary:
                highest_salary_emp = emp
        highest_salary_emp.info()

company = Company()
while True:
    print("1. Добави служител")
    print("2. Покажи всички служители")
    print("3. Покажи общ разход за заплати")
    print("4. Покажи служителя с най-висока заплата")
    print("5. Покажи всички мениджъри")
    print("0. Изход")
    choice = int(input("Избор: "))

    if choice == 1:
        employee_name = input("Име: ")
        employee_position = input("Позиция: ")
        employee_salary = int(input("Заплата: "))
        employee = Employee(employee_name, employee_position, employee_salary)
        company.add_employee(employee)
    if choice == 2:
        for emp in company.employees:
            emp.info()
    if choice == 3:
        print(f"Общия разход за заплати: {company.total_salary()}")
    if choice == 4:
        company.highest_salary()
    if choice == 5:
        company.manager()
    if choice == 0:
        break




