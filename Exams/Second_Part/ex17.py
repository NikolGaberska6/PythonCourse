class Device:
    def __init__(self, serial_number, name, brand, price, stock):
        self.serial_number = serial_number
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            print(f"Продадохте {quantity} броя устройства на дадената марка.")
            self.stock -= quantity
            print(f"Новата наличност на устройствата след продажбата е: {self.stock} бр.")
        else:
            print("Недостатъчнан наличност! Неуспешна продажба!")

    def discount(self):
        if 500 < self.price <= 1000:
            discount = 0.06 * self.price
            print("Отстъпката е 6% от цената на устройството.")
            self.price -= discount
            print(f"Новата цена с отстъпката е: '{self.price:.2f}' лв.")
        elif 200 <= self.price <= 500:
            discount = 0.1 * self.price
            print("Отсъпката е 10% от цената на устройството.")
            self.price -= discount
            print(f"Новата цена с отстъпката е: '{self.price:.2f}' лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената на устройството без отстъпка е: '{self.price:.2f}' лв.")

    def info(self):
        print(f"Сериен номер: {self.serial_number}, Име: {self.name}, "
              f"Марка: {self.brand}, Цена: {self.price}, Количество: {self.stock}.")

def search_by_serial_number(device_list, serial_number):
    for device in device_list:
        if device.serial_number == serial_number:
            print("Намерихме устройството с посочения сериен номер в списъка с устройства.")
            device.info()
            return
    print("Няма устройство с посочения сериен номер в списъка с устройства!")

def search_by_brand(device_list, brand):
    devices_of_brand = []
    for device in device_list:
        if device.brand == brand:
            devices_of_brand.append(device)

    average_sum_of_brand = 0
    sum_of_every_device = 0
    if len(devices_of_brand) > 0:
        for device in devices_of_brand:
            sum_of_every_device += device.price
        average_sum_of_brand = sum_of_every_device / len(devices_of_brand)
        print(f"Средната цена на устройствата на посочената марка е: "
              f"'{average_sum_of_brand:.2f}' лв.")
    else:
        print("Няма намерени устройства в списъка на посочената марка!")

    devices_with_smaller_price = []
    for device in devices_of_brand:
        if device.price <= average_sum_of_brand:
            devices_with_smaller_price.append(device)

    if len(devices_with_smaller_price) > 0:
        print("Продукти в списъка с цена ≤ средната за марката: ")
        for device in devices_with_smaller_price:
            device.info()
    else:
        print("Няма устройства в списъка с цена ≤ средната за марката!")

def sort_by_stock(device_list):
    device_list.sort(key=lambda d: d.stock)
    print("Сортирахте списъка във възходящ ред!")

def delete_by_name(device_list, name):
    for device in device_list.copy():
        if device.name == name:
            if device.stock <= 2:
                print(f"Изтрихте продукта '{name}' от списъка с устройства.")
                device_list.remove(device)

def main():
    device_list = []
    n = int(input("Въведете колко устройства искате да добавите: "))
    for i in range(n):
        serial_number = input("Въведете сериен номер на устройството: ")
        name = input("Въведете име на устройството: ")
        brand = input("Въведете марка на устройството: ")
        price = float(input("Въведете цена на устройството: "))
        stock = int(input("Въведете количество на устройството: "))
        device = Device(serial_number, name, brand, price, stock)
        device_list.append(device)
        print("Успешно добавихте устройството към списъка с устройства!")


    found = False
    serial_number = input("Веведете сериения номер на устройството, който искате да продавате: ")
    for device in device_list:
        if device.serial_number == serial_number:
            found = True
            quantity = int(input("Въведете количеството устройства, което искате да продадете: "))
            device.sell(quantity)
            break
    if not found:
        print("Няма устройства с посочения сериен номер в списъка с устросйтва!")

    found = False
    serial_number = input("Веведете сериения номер на устройството, което искате да проверите за отстъпка: ")
    for device in device_list:
        if device.serial_number == serial_number:
            found = True
            device.discount()
    if not found:
        print("Няма устройства с посочения сериен номер в списъка с устройства!")

    serial_number = input("Веведете сериения номер на устройството, което търсите: ")
    search_by_serial_number(device_list, serial_number)

    brand = input("Въведете марката на устройството, което търсите: ")
    search_by_brand(device_list, brand)

    sort_by_stock(device_list)

    name = input("Въведете името на устройството, което искате да изтриете!")
    delete_by_name(device_list, name)

main()