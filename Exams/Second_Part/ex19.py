class Order:
    def __init__(self, order_id, product_name, category, price, quantity):
        self.order_id = order_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity = quantity

    def add_items(self, count):
        self.quantity += count
        print("Добавихте елемент към количеството на поръчката!")

    def discount(self):
        if 100 < self.price <= 300:
            discount = 0.05 * self.price
            print("Отстъпката е 5% от цената на поръчката!")
            self.price -= discount
            print(f"Новата цена на поръчката с отстъпката е: {self.price:.2f} лв.")
        elif 50 <= self.price <= 100:
            discount = 0.1 * self.price
            print("Отстъпката е 10% от цената на поръчката!")
            self.price -= discount
            print(f"Новата цена на поръчката с отстъпката е: {self.price:.2f} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената без отстъпката е: {self.price:.2f} лв.")

    def info(self):
        print(f"ИД на продукта: {self.order_id}, Име: {self.product_name},"
              f"Категория: {self.category}, Цена: {self.price}, "
              f"Количество: {self.quantity}.")

def	search_by_order_id(order_list, order_id):
    for order in order_list:
        if order.order_id == order_id:
            print("Поръчката с посоченото ИД е намерена!")
            print("Информация за поръчката: ")
            order.info()
            return
    print("Не намерихме поръчка с посоченото ИД!")

def search_by_category(order_list, category):
    order_of_given_category = []
    for order in order_list:
        if order.category == category:
            order_of_given_category.append(order)

    sum_of_price = 0
    average_of_price = 0
    if len(order_of_given_category) > 0:
        for order in order_of_given_category:
            sum_of_price += order.price
        average_of_price = sum_of_price/len(order_of_given_category)
        print(f"Средната цената на поръчките от дадената категория е: {average_of_price:.2f} лв.")
    else:
        print("Няма поръчка от дадената категория!")

    prices_lower_than_average = []
    for order in order_of_given_category:
        if order.price <= average_of_price:
            prices_lower_than_average.append(order)

    if len(prices_lower_than_average) > 0:
        print("Всички поръчки от дадената категория с цена ≤ средната за категорията: ")
        for order in prices_lower_than_average:
            order.info()
    else:
        print("Няма поръчки от дадената категория с цена ≤ средната за категорията!")

def sort_by_quantity(order_list):
    order_list.sort(key=lambda o: o.quantity)
    print("Сортирахте списъка с поръчки във възходящ ред!")

def delete_by_product_name(order_list, product_name):
    for order in order_list.copy():
        if order.product_name == product_name:
            if order.quantity <= 3:
                print(f"Успешно изтрихте поръчката с име '{product_name}' от листа с поръчки!")
                order_list.remove(order)

def main():
    order_list = []
    n = int(input("Въведете броя на поръчките, които ще добавите: "))
    for i in range(n):
        order_id = input("Въведете ИД-то на поръчката: ")
        product_name = input("Въведете името на продукта: ")
        category = input("Въведете категорията: ")
        price = float(input("Въведете цената на поръчката: "))
        quantity = int(input("Въведете количеството на поръчката: "))
        order = Order(order_id, product_name, category, price, quantity)
        order_list.append(order)
        print("Успешно добавихте поръчката към списъка с поръчки!")

    found = False
    order_id = input("Въведете ИД-то на поръчката към която искате да добавяте елементи: ")
    for order in order_list:
        if order.order_id == order_id:
           found = True
           count = int(input("Въведете колко елемента искате да добавите: "))
           order.add_items(count)
           break
    if not found:
        print("Не намерихме поръчка с посоченото ИД в списъка с поръчки!")

    found = False
    order_id = input("Въведете ИД-то на поръчката, която искате да проверите за отстъпка: ")
    for order in order_list:
        if order.order_id == order_id:
            found = True
            order.discount()
            break
    if not found:
        print("Не намерихме поръчка с посоченото ИД в списъка с поръчки!")

    order_id = input("Въведете ИД-то на поръчката, която търсите: ")
    search_by_order_id(order_list, order_id)

    category = input("Въведете категорията на поръчката, по която търсите: ")
    search_by_category(order_list, category)

    sort_by_quantity(order_list)

    product_name = input("Въведете името на продукта, който искате да изтриете: ")
    delete_by_product_name(order_list, product_name)

main()