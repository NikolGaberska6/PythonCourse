class Animal:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def birthday(self):
        self.age += 1
        print(f"Увеличихте годините на {self.name} с една!")
        print(f"Годините на {self.name} са: {self.age}")

    def info(self):
        print(f"Име: {self.name}, Тип: {self.animal_type}, "
              f"Години: {self.age}")

animal_list = []
while True:
    print("----------------")
    print("       MENU     ")
    print("----------------")
    print("1.Добавяне на животно")
    print("2.Рожден ден")
    print("3.Всички животни")
    print("0.Изход")
    choice = int(input("Въведете своя избор: "))

    if choice == 1:
        name = input("Въведете името на животното: ")
        animal_type = input("Въведете типа на животното: ")
        age = int(input("Въведете годините на животното: "))
        animal = Animal(name, animal_type, age)
        animal_list.append(animal)
        print(f"Добавихте {animal.name} към листа с животно!")

    elif choice == 2:
        name = input("Въведете името на животното, "
                     "което има рожден ден: ")
        for animal in animal_list:
            if animal.name == name:
                animal.birthday()

    elif choice == 3:
        for animal in animal_list:
            animal.info()

    elif choice == 0:
        print("Довиждане!")
        break