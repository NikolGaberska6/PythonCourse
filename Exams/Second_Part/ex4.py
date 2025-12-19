class Electronics:
    def __init__(self, serial, name, brand, price, stock):
        self.serial = serial
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if self.stock > quantity:
            self.stock = self.stock - quantity
            print(f"Продадохте {quantity} количество.")
        else:
            print("Недостатъчна наличност!")

    def apply_discount(self):
        if 100 < self.price < 500:
            discount = self.price * 0.08
            print(f"Отстъпката е {discount}.")
            self.price = self.price - discount
            print(f"Новата цена е: {self.price} лв.")
        elif 50 < self.price < 100:
            discount = self.price * 0.05
            print(f"Отстъпката е {discount}")
            self.price = self.price - discount
            print(f"Новата цена е: {self.price} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената е: {self.price} лв.")

    def info(self):
        print(f"Сериен номер: {self.serial}, Име: {self.name}, Марка: {self.brand}, "
              f"Цена: {self.price}, Наличност: {self.stock}")

electronic_list = []
n = int(input("Въведете броя на продуктите, които искате да въведете: "))
for i in range(n):
    print("-----------Добавяне на продукт------------")
    serial = input("Сериен номер: ")
    name = input("Име: ")
    brand = input("Марка: ")
    price = float(input("Цена: "))
    stock = input("Наличност (налична, неналична): ")
    product = Electronics(serial, name, brand, price, stock)
    electronic_list.append(product)
    print("Успешно добавяне на продукта!")

def search_by_serial(electronics, serial):
    for electronic in electronic_list:
        if electronic.serial.lower() == serial.lower():
            electronic.info()

def filter_by_brand(electronics, brand):
    products_by_brand = []
    for product in electronic_list:
        if product.brand.lower() == brand.lower():
            products_by_brand.append(product)

    total_price = 0
    for product in products_by_brand:
        total_price += product.price
    if len(products_by_brand) == 0:
        print(f"Няма продукти на марката: {brand}.")

    average = total_price / len(products_by_brand)
    print(f"Средната цена на продуктите на марката е: {average}")

    result = []
    for product in products_by_brand:
        if product.price <= average:
            result.append(product)

    if len(result) > 0:
        print("Продукти с цена <= средната цена:")
        for product in result:
            product.info()
    else:
        print("Няма книги с цена по-ниска или равна на средната.")

def delete_low_stock(electronics, name):
    count = 0
    for product in electronic_list:
        if product.name == name:
            count += 1
    if count != 0 and count<= 3:
       electronic_list.remove(product)
       print(f"Изтрихте продукта от листа")

    for product in electronic_list:
        product.info()


serial = input("Въведете сериен номер, по който търсите: ")
search_by_serial(electronic_list, serial)
brand = input("Въведете марката, по която искате да филтрирате: ")
filter_by_brand(electronic_list, brand)
name = input("Въведете името на продукта, който искате да изтриете: ")
delete_low_stock(electronic_list, name)