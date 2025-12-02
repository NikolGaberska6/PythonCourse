class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def apply_discount(self, percent):
        discount = self.price * percent/100
        print(f"Намалихте цената с продукта с {percent} процента!")
        self.price = self.price - discount
        print(f"Новата цена на продукта е: {self.price}")

    def sell(self, amount):
        if amount > self.quantity:
            print("Недостатъчна наличност!")
        else:
            self.quantity -= amount
            print(f"Намалихте наличността с {amount}.")
            print(f"Новата наличност на '{self.name}' е {self.quantity} броя")

    def info(self):
        print(f"{self.name}, {self.price}, {self.quantity}, {self.category}")

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Добавихте '{product.name}' в списъка с продукти!")

    def search_by_category(self, category):
        print(f"Продуктите от категория {category} ca: ")
        for p in self.products:
            if p.category.lower() == category.lower():
                print(p.info)

    def out_of_stock(self):
        print("Изчерпаните продукти са: ")
        for p in self.products:
            if p.quantity == 0:
                print(p.info)

    def most_expensive(self):
        most_expensive = self.products[0]
        for p in self.products:
            if p.price > most_expensive.price:
                most_expensive = p
        print(f"Най-скъпият продукт е: {most_expensive.info}")

    def sell_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                amount = int(input("Какво количество искате да продадете: "))
                p.sell(amount)

    def discount(self, name):
        for p in self.products:
            if p.name == name:
                percent = int(input("Въведете процента на отстъпката: "))
                p.apply_discount(percent)

    def category(self, category):
        for p in self.products:
            print("Всички продукти от дадената категория са: ")
            if p.category == category:
                print(p.name)

store = Store()
while True:
  print("1.Добавяне на продукт")
  print("2.Продажба")
  print("3.Отстъпки")
  print("4.Категория")
  print("5.Изход")
  choice = int(input("Изберете опция: "))

  if choice == 1:
      name = input("Име: ")
      price = float(input("Цена: "))
      quantity = int(input("Количество: "))
      category = input("Категория: ")
      product = Product(name, price, quantity, category)
      store.add_product(product)

  if choice == 2:
      name = input("Въведете продукта, който искате да продадете: ")
      store.sell_product(name)

  if choice == 3:
      name = input("Въведете продукта, на който искате да направите отстъпка: ")
      store.discount(name)

  if choice == 4:
      category = input("Въведете категорията, чиито продукти искате да принтирате: ")
      store.category(category)

  if choice == 5:
      print("Довиждане!")
      break

