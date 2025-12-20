class BookOrder:
    def __init__(self, order_num, title, author, quantity, status):
        self.order_num = order_num
        self.title = title
        self.author = author
        self.quantity = quantity
        self.status = status

    def display(self):
        print("Цялата информация за поръчката: ")
        print(f"Номер на поръчката: {self.order_num},"
              f"Заглавие на книгата: {self.title}, Автор: {self.author},"
              f"Бройки: {self.quantity}, Статус: {self.status}")

    def update_quantity(self):
        new_quantity = int(input("Въведете новото количество: "))
        self.quantity = new_quantity
        print("Успешно променихте количеството!")

orders = []
def input_order():
    print("------Добавяне на поръчка------")
    order_num = int(input("Номер на поръчката: "))
    title = input("Заглавие на книгата: ")
    author = input("Автор на книгата: ")
    quantity = int(input("Бройки: "))
    status = input("Статус: ")
    return BookOrder(order_num, title, author, quantity, status)

def search_order(orders, order_num):
    for order in orders:
        if order.order_num == order_num:
            print("Found!")
            print(f"Статус: {order.status}")
            return
    print("Not Found!")

def add_order(orders, new_order):
    orders.append(new_order)
    print("Успешно добавихте поръчката!")

#-----------ОСНОВНА ПРОГРАМА---------------
def main():
  n = int(input("Въведете колко поръчки ще въведете: "))
  for i in range(n):
    new_order = input_order()
    add_order(orders, new_order)

  order_num = int(input("Въведете номера на поръчката, която търсите: "))
  search_order(orders, order_num)

  new_order = input_order()
  add_order(orders, new_order)

main()