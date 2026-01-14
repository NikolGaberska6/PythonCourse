
class FoodDelivery:
    def __init__(self, order_number, destination, price, delivery_term, order_status):
        self.order_number = order_number
        self.destination = destination
        self.price = price
        self.delivery_term = delivery_term
        self.order_status = order_status

    def order_info(self):
        print("Цялата информация за поръчката: ")
        print(f"Номер: {self.order_number}, Място на получаване: {self.destination}, "
              f"Цена: {self.price}, Срок на доставка: {self.delivery_term}, "
              f"Статус на поръчката: {self.order_status}.")

    def change_term(self):
        new_term = input("Въведете нов срок на доставката: ")
        self.delivery_term = new_term
        print("Успешно променихте срока на доставката!")

def input_order():
    print("Моля въведете данните за поръчката, която искате да направите!")
    order_number = int(input("Въведете номера на поръчката: "))
    destination = input("Въведете място на получаване на поръчката: ")
    price = float(input("Въведете цената на поръчката: "))
    delivery_term = input("Въведете срока на доставка на поръчката: ")
    order_status = input("Въведете статуса на поръчката: ")
    return FoodDelivery(order_number, destination, price, delivery_term, order_status)

def status_info(order_list, num):
    for order in order_list:
        if order.order_number == num:
            found = True
            print("Found!")
            print(f"Статуса на поръчката е: {order.order_status}.")
            return
    print("Not found!")

def add_order(order_list, new_order):
    order_list.append(new_order)
    print("Успешно добавихте поръчката към списъка с поръчки!")

def main():
    order_list = []
    n = int(input("Въведете броя на поръчките, които искате да добавите: "))
    for i in range(n):
        order = input_order()
        order_list.append(order)
        print(f"Успешно добавихте поръчката с номер {order.order_number} списъка с поръчки!")

    order_number = int(input("Въведете номера на поръчката, чиито срок за доставка искате да промените: "))
    found = False
    for order in order_list:
        if order.order_number == order_number:
            found = True
            order.change_term()
    if not found:
        print("Няма поръчка с посочения номер в списъка с поръчки!")

    num = int(input("Въведете номера на поръчката, по който търсите: "))
    status_info(order_list, num)

    print("Добавяне на поръчка!")
    new_order = input_order()
    add_order(order_list, new_order)

main()