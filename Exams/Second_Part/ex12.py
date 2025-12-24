class Medicine:
    def __init__(self, code, name, producer, price, stock):
        self.code = code
        self.name = name
        self.producer = producer
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if self.stock >= quantity:
            print(f"Успешно продадохте {quantity} количество от продукта!")
            self.stock -= quantity
            print(f"Новото количество: {self.stock}")

    def discount(self):
        if 20 < self.price <= 50:
            discount = 0.06 * self.price
            print("Остъпката е 6% от цената!")
            self.price -= discount
            print(f"Новата цена е: {self.price} лв.")
        elif 5 <= self.price <= 20:
            discount = 0.1 * self.price
            print("Остъпката е 10% от цената!")
            self.price -= discount
            print(f"Новата цена е: {self.price} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената си остава същата: {self.price} лв.")

    def info(self):
        print("Цялата информация за поръчката: ")
        print(f"Код: {self.code}, Име: {self.name}, Производител: {self.producer}, "
              f"Цена: {self.price}, Количество: {self.stock}.")

def search_by_code(medicine_list, code):
    for medicine in medicine_list:
        if medicine.code == code:
            print("Поръчката е намерена!")
            medicine.info()
            return
    print("Грешка! Поръчка с този код не съществува!")

def search_by_producer(medicine_list, producer):
    products_by_producer = []
    for medicine in medicine_list:
        if medicine.producer == producer:
            products_by_producer.append(medicine)

    average = 0
    sum_of_products = 0
    if len(products_by_producer) > 0:
        for product in products_by_producer:
            sum_of_products += product.price
        average = sum_of_products  / len(products_by_producer)
    else:
        print("Няма продукти на този производител!")

    total = []
    for product in products_by_producer:
        if product.price <= average:
            total.append(product)

    if len(total) > 0:
      print("Продукти с цена ≤ средната за производителя: ")
      for product in total:
         product.info()
    else:
        print("Няма продукти с цена ≤ средната за производителя!")

def sort_by_stock(medicine_list):
    medicine_list.sort(key=lambda m: m.stock)
    print("Сортирахте листа във възходящ ред!")

def delete_by_name(medicine_list, name):
    for medicine in medicine_list.copy():
        if medicine.name == name and medicine.stock <= 5:
            print(f"Успешно изтрихте {medicine.name} от листа!")
            medicine_list.remove(medicine)

#------------Основна програма--------------
def main():

  medicine_list = []
  n = int(input("Въведете броч на продуктите, които ще въведете: "))
  for i in range(n):
    print("-------Добавяне на продукт-------")
    code = input("Въведете кода на продукта: ")
    name = input("Въведете името на продукта: ")
    producer = input("Въведете производителя на продукта: ")
    price = float(input("Въведете цената на продукта: "))
    stock = int(input("Въведете количеството на продукта: "))
    medicine = Medicine(code, name, producer, price, stock)
    medicine_list.append(medicine)
    print("Успешно добавихте продукта към списъка.")

  code = input("Въведете кода на продукта, от който искате да продавате: ")
  quantity = int(input("Въведете количеството, което искате да продадете: "))
  for medicine in medicine_list:
    if medicine.code == code:
        medicine.sell(quantity)

  code = input("Въведете кода на продукта, по който търсите: ")
  search_by_code(medicine_list, code)

  producer = input("Въведете прозиводителя, по който търсите: ")
  search_by_producer(medicine_list, producer)

  sort_by_stock(medicine_list)

  name = input("Въведете името на продукта, който искате да изтриете: ")
  delete_by_name(medicine_list, name)

main()