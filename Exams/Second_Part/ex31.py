class OnlineOrder:
    def __init__(self, order_id, customer, product_name, price, quantity, status):
        self.order_id = order_id
        self.customer = customer
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.status = status

    def change_status(self, new_status):
        print("Променихте статуса на дадената поръчка!")
        print(f"Нов статус: {new_status}")
        self.status = new_status

    def total_price(self):
        total = self.price * self.quantity
        print(f"Крайната цена на поръчката е: {total:.2f}")
        return total

    def info(self):
        print(f"ID: {self.order_id}, Име на клиента: {self.customer}, "
              f"Име на продукта: {self.product_name}, Цена на продукта: {self.price}, "
              f"Брой поръчани бройки: {self.quantity}, Статус: {self.status}.")

def search_by_order_id(orders, order_id):
    for order in orders:
        if order.order_id == order_id:
            order.info()
            return
    print("Не е намерена поръчка с посоченото ID!")

def orders_above_average(orders):
    sum_of_all_prices = 0
    count_quantity = 0
    for order in orders:
        sum_of_all_prices += order.total_price()
        count_quantity += order.quantity
    average = sum_of_all_prices/count_quantity
    print(f"Средната крайна цена на всички поръчки е: {average:.2f} лв.")

    above_average = []
    for order in orders:
        if order.total_price() > average:
            above_average.append(order)
    if len(above_average) > 0:
        print("Списакът с поръчки, чиято крайна цена е по-висока от средната: ")
        for order in above_average:
            order.info()
    else:
        print("Няма поръчки, чиято крайна цена е по-висока от средната!")

    return above_average

def sort_by_quantity(orders):
    orders.sort(key=lambda o: o.quantity)
    print("Сортирахте поръчките по брой поръчани бройки във възходящ ред!")
    print("Сортирания списък: ")
    for order in orders:
        order.info()
    return orders

def delete_cancelled_orders(orders):
    deleted_orders = 0
    for order in orders.copy():
        if order.status == "cancelled":
            deleted_orders += 1
            print(f"Изтрихте поръчката с номер {order.order_id} от списъка!")
            orders.remove(order)
    if deleted_orders != 0:
        print(f"Броят на поръчките със статус „cancelled“ е: {deleted_orders}.")
    else:
        print("Няма поръчки със статус „cancelled“ в листа!")

def main():
    orders = []
    n = int(input("Въведете броя на поръчките, които искате да добавите: "))
    for i in range(n):
        order_id = input("Въведете айдито на поръчката, която искате да добавите: ")
        customer  = input("Въведете името на клиента на поръчката, която искате да добавите: ")
        product_name = input("Въведете името на продукта на поръчката, която искате да добавите: ")
        price = float(input("Въведете цената на поръчката, която искате да добавите: "))
        quantity = int(input("Въведете брой поръчани бройки на поръчката, която искате да добавите: "))
        status = input("Въведете статус на поръчката, която искате да добавите: ")
        order = OnlineOrder(order_id, customer, product_name, price, quantity, status)
        orders.append(order)
        print("Успешно добавихте поръчката в списъка с поръчки!")

    found = False
    order_id = input("Въведете айдито на поръчката, на която искате да промените статуса: ")
    for order in orders:
        if order.order_id == order_id:
            found = True
            new_status = input("Въведете новия статус на поръчката: ")
            order.change_status(new_status)
    if not found:
        print("Не е намерена поръчка с посоченото ID в списъка с поръчки!")

    found = False
    order_id = input("Въведете айдито на поръчката, на която искате да разберете крайната цена: ")
    for order in orders:
        if order.order_id == order_id:
            found = True
            order.total_price()
    if not found:
        print("Не е намерена поръчка с посоченото ID в списъка с поръчки!")

    order_id = input("Въведете айдито на поръчката, която търсите: ")
    search_by_order_id(orders, order_id)

    orders_above_average(orders)

    sort_by_quantity(orders)

    delete_cancelled_orders(orders)

main()