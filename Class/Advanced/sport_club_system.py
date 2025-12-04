class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.membership_active = True

    def activate(self):
        if not self.membership_active:
            self.membership_active = True
            print(f"Членството на {self.name} е вече активно!")
        else:
            print(f"Членството на {self.name} е от преди активно!")

    def deactivate(self):
        if self.membership_active:
            self.membership_active = False
            print(f"Членството на {self.name} е деактивирано!")
        else:
            print(f"Членството на {self.name} е от преди деактивирано!")

    def info(self):
        if self.membership_active:
            status = "активитрано"
        else:
            status = "деактивирано"
        print(f"Име: {self.name}, Години: {self.age}, Статус: {status}")

membership_list = []
while True:
    print("------------------")
    print("        MENU      ")
    print("------------------")
    print("1.Добавяне на член")
    print("2.Активиране")
    print("3.Деактивиране")
    print("4.Всички членове")
    print("5.Изход")
    choice = int(input("Въведете вашия избор: "))

    if choice == 1:
        name = input("Въведете името на члена: ")
        age = int(input("Въведете годините на члена: "))
        person = Member(name, age)
        membership_list.append(person)
    elif choice == 2:
        name = input("Въведете името на члена, чиито статус искате да активирате: ")
        for member in membership_list:
            if member.name == name:
                member.activate()
    elif choice == 3:
        name = input("Въведете името на члена, чиито статус искате да деактивирате: ")
        for member in membership_list:
            if member.name == name:
                member.deactivate()
    elif choice == 4:
        for member in membership_list:
            member.info()
    elif choice == 5:
        print("Довиждане!")
        break
