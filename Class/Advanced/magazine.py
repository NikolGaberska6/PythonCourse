class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def restock(self, amount):
        if amount > 0:
            self.quantity += amount
            print(f"Добавихте {amount} към продукта: {self.name}")
            print(f"Новото количество е: {self.quantity}") 

    def buy(self, amount):
        if self.quantity > amount:
            self.quantity = self.quantity - amount
            print(f"Закупихте {amount} количество от продукта {self.name}")
            print(f"Новото количество е: {self.quantity}")
        else:
            print("Недостатъчна наличност!")

    def info(self):
        print(f"Име: {self.name}, "
              f"Цена: {self.price}, "
              f"Количество: {self.quantity}")

products = []
while True:
    print("----------------------")
    print("          МЕНЮ        ")
    print("----------------------")
    print("1.Добавяне на продукт")
    print("2.Покупка на продукт")
    print("3.Зареждане на продукт")
    print("4.Всички продукти")
    print("0.Изход")
    choice = int(input("Въведете своя избор: "))

    if choice == 1:
        name = input("Въведете името на продукта, който искате да добавите: ")
        quantity = int(input("Въведете количеството на продукта, който искате да добавите: "))
        price = int(input("Въведете цената на продукта, който искате да добавите: "))
        product = Product(name, quantity, price)
        products.append(product)

    elif choice == 2:
        name = input("Въведете продукта, от който искате да закупите: ")
        amount = int(input("Въведете количеството, което искате да закупите: "))
        for p in products:
            if p.name == name:
                p.buy(amount)

    elif choice == 3:
        name = input("Въведете продукт, от който искате да заредите: ")
        amount = int(input("Въведете количеството, което искате да заредите: "))
        for p in products:
            if p.name == name:
                p.restock(amount)

    elif choice == 4:
        print("Всички продукти са: ")
        for p in products:
            p.info()

    elif choice == 0:
        print("Довиждане!")
        break