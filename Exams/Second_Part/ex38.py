class CourierPackage:
    def __init__(self, package_number, sender, receiver, weight, delivery_status):
        self.package_number = package_number
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
        self.delivery_status = delivery_status

    def package_info(self):
        print("----Пълна информация за пратката----")
        print(f"Номер: {self.package_number}, Подател: {self.sender}, "
              f"Получател: {self.receiver}, Тегло: {self.weight},"
              f"Статус: {self.delivery_status}.")

    def change_status(self):
        print("----Промяна на статуса на пратката----")
        new_status = input("Въведете новия статус на пратката: ")
        self.delivery_status = new_status
        print("Статуса е променен успешно!")

def input_delivery():
    print("----Добавяне на пратка----")
    package_number = int(input("Въведете номера на пратката: "))
    sender = input("Въведете подател: ")
    receiver = input("Въведете получател: ")
    weight = float(input("Въведете тегло: "))
    delivery_status = input("Въведете статус (доставена, в процес, отказана): ")
    return CourierPackage(package_number, sender, receiver, weight, delivery_status)

def find_package(package_list, num):
    for package in package_list:
        if package.package_number == num:
            print("Found!")
            print(f"Статус: {package.delivery_status}")
            return
    print("Not Found!")

def add_package(package_list, new_package):
    package_list.append(new_package)
    print("Успешно добавихте поръчката към списъка с поръчки!")

def main():
    package_list = []
    n = int(input("Въведете броя на поръчките, които искате да добавите: "))
    for i in range(n):
        package = input_delivery()
        package_list.append(package)
        print("Успешно добавихте поръчката в списъка!")

    found = False
    package_number = int(input("Въведете номера на пратката, "
                               "на която искате да смените статуса: "))
    for package in package_list:
        if package.package_number == package_number:
            found = True
            package.change_status()
    if not found:
        print("Няма поръчка с посочения номер в списъка!")

    num = int(input("Въведете номера на пратката, по която търсите: "))
    find_package(package_list, num)

    new_package = input_delivery()
    add_package(package_list, new_package)
    
main()