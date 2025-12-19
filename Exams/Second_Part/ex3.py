class FoodDelivery:
    def __init__(self,order_number, destination, price, delivery_term, order_status):
        self.order_number = order_number
        self.destination = destination
        self.price = price
        self.delivery_term = delivery_term
        self.order_status = order_status

    def order_info(self):
        print("Информация за поръчката: ")
        print(f"Номер: {self.order_number}, Място на получаване: {self.destination}",
              f"Цена: {self.price}, Срок за получаване: {self.delivery_term},"
              f"Статус: {self.order_status}")

    def change_term(self):
        new_term = input("Въведете нов срок за доставката: ")
        self.delivery_term = new_term
        print("Срокът за доставката е променен успешно!")


def input_order():
    order_number = input("Номер на поръчка: ")
    destination = input("Място на получаване: ")
    price = float(input("Цена: "))
    delivery_term = input("Срок на доставка: ")
    order_status = input("Статус (доставена, забавена, отказана): ")
    return FoodDelivery(order_number, destination, price, delivery_term, order_status) #object

def status_info(order_list, num):
    for order in order_list:
        if order.order_number == num:
            print("Found")
            print(f"Статус: {order.order_status}")
            return
    print("Not Found!")

def add_order(order_list, new_order):
    order_list.append(new_order)
    print("Успешно добавена поръчка!")

# -------- ОСНОВНА ПРОГРАМА --------

def main():
    order_list = []
    n = int(input("Въведете брой поръчки: "))
    for i in range(n):
        order = input_order()
        order_list.append(order)
        print("Успешно добавихте поръчката в листа!")

    num = input("Въведете номера на поръчката, по която търсите: ")
    status_info(order_list, num)

    print("Добавяне на нова поръчка: ")
    new_order = input_order()
    add_order(order_list, new_order)

main()
