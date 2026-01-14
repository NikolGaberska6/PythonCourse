class Order:
    def __init__(self, order_id, client_name, dish, price):
        self.order_id = order_id
        self.client_name = client_name
        self.dish = dish
        self.price = price

    def order_info(self):
        print("---Информация за поръчката---")
        print(f"ИД: {self.order_id}, Име на клиента: {self.client_name}, "
              f"Ястие: {self.dish}, Цена: {self.price}.")

    def change_price(self):
        print("----Промяна на цената на поръчката----")
        new_price = float(input("Въведете новата цена на поръчката: "))
        self.price = new_price
        print("Цената бе успешно променена!")

def order_input():
    print("---Добавяне на поръчка---")
    order_id = input("Въведете ИД-то на поръчката: ")
    client_name = input("Въведете името на клиента: ")
    dish = input("Въведете ястието: ")
    price = float(input("Въведете цената на поръчката: "))
    return Order(order_id, client_name, dish, price)

def search_by_client(order_list, client_name):
    orders_by_client = []
    for order in order_list:
        if order.client_name == client_name:
            orders_by_client.append(order)
    if len(orders_by_client) > 0:
        print("Всички поръчки на посочения клиент: ")
        for order in orders_by_client:
            order.order_info()
    else:
        print("Orders not found")

def add_order(order_list, new_order):
    order_list.append(new_order)
    print("Успешно добавихте поръчката в списъка!")

def main():
    order_list = []
    n = int(input("Въведете броя на поръчките, които искате да добавите: "))
    for i in range(n):
        order = order_input()
        order_list.append(order)
        print("Успешно добавихте поръчката в списъка!")

    found = False
    order_id = input("Въведете ИД-то на поръчката, "
                     "чиято цена искате да промените: ")
    for order in order_list:
        if order.order_id == order_id:
            found = True
            print("Поръчката е намерена!")
            order.change_price()
    if not found:
        print("Не е намерена поръчка с посоченото ИД!")

    client_name = input("Въведете името на клиента, чиито поръчки търсите: ")
    search_by_client(order_list, client_name)

    new_order = order_input()
    add_order(order_list, new_order)

main()