class BookOrder:
    def __init__(self, order_number, customer_name, book_title,
                 price, order_status):
        self.order_number = order_number
        self.customer_name = customer_name
        self.book_title = book_title
        self.price = price
        self.order_status = order_status

    def order_info(self):
        print("----Информация за поръчката----")
        print(f"Номер на поръчката: {self.order_number},"
              f"Име на клиент: {self.customer_name}, "
              f"Заглавие на книгата: {self.book_title}, Цена: {self.price}, "
              f"Статус на поръчката: {self.order_status}.")

    def change_price(self):
        print("----Промяна на цената на поръчката----")
        new_price = float(input("Въведете новата цена на поръчката: "))
        self.price = new_price
        print("Цената бе успешно сменена!")

def input_order():
    print("----Добавяне на поръчка----")
    order_number = int(input("Въведете номера на поръчката: "))
    customer_name = input("Въведете името на клиента: ")
    book_title = input("Въведете заглавието на книгата: ")
    price = float(input("Въведете цената на поръчката: "))
    order_status = input("Въведете статуса на поръчката "
                         "(изпълнена, в процес, отказана): ")
    return BookOrder(order_number, customer_name, book_title, price, order_status)

def status_info(order_list, num):
    for order in order_list:
        if order.order_number == num:
            print("Found!")
            print(f"Статус: {order.order_status}.")
            return
    print("Not Found!")

def add_order(order_list, new_order):
    order_list.append(new_order)
    print("Успешно добавихте поръчката към списъка!")

def main():
    order_list = []
    n = int(input("Въведете броя на поръчките, които искате да добавите: "))
    for i in range(n):
        order = input_order()
        order_list.append(order)
        print("Поръчката е успешно добавена в листа!")

    found = False
    order_number = int(input("Въведете номера на поръчката, чиято цена искате да промените: "))
    for order in order_list:
        if order.order_number == order_number:
            found = True
            order.change_price()
    if not found:
        print("Не е намерена поръчка с посочения номер!")

    num = int(input("Въведете номера на поръчката, по който търсите: "))
    status_info(order_list, num)

    new_order = input_order()
    add_order(order_list, new_order)

main()