class Package:
    def __init__(self, id, recipient, weight, delivery_time, status):
        self.id = id
        self.recipient = recipient
        self.weight = weight
        self.delivery_time = delivery_time
        self.status = status

    def info(self):
        print("Цялата информация за пратката: ")
        print(f"ИД: {self.id}, Получател: {self.recipient},"
              f"Тегло: {self.weight}, Време за доставка: {self.delivery_time},"
              f"Статус: {self.status}.")

    def update_time(self):
        new_time = input("Въведете ново време за доставка: ")
        self.delivery_time = new_time
        print("Успешно променихте времето за доставка!")

package_list = []
def input_info():
    print("------Добавяне на поръчка-----")
    id = input("Въвдете ID: ")
    recipient = input("Въведете получател: ")
    weight = int(input("Въведете тегло: "))
    delivery_time = input("Въведете време за доставка: ")
    status = input("Въведете статус (изпратена, получена): ")
    return Package(id, recipient, weight, delivery_time, status)

def find_package(package_list, id):
    for package in package_list:
        if package.id == id:
            print("Found!")
            print(f"Статус: {package.status}")
            return
    print("Not Found!")


def add_package(package_list, new_package):
    package_list.append(new_package)
    print("Успешно добавихте поръчката!")

#----------ОСНОВНА ПРОГРАМА------------
def main():
   n = int(input("Въведете броя на поръчките, които ще добавите: "))
   for i in range(n):
     new_package = input_info()
     add_package(package_list, new_package)

   id = input("Въвдете ID-то, по което търсите: ")
   find_package(package_list, id)

   new_package = input_info()
   add_package(package_list, new_package)

main()