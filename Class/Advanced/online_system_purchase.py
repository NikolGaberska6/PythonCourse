class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.is_completed = False

    def add_items(self, item):
        self.items.append(item)
        print(f"Добавихте {item} към списъка с продукти на номер {self.order_id}")

    def complete(self):
        if not self.is_completed:
            self.is_completed = True
            print(f"Поръчката с номер {self.order_id} е завършена!")

    def info(self):
        if self.is_completed:
            status = "завършена"
        else:
            status = "незавършена"
        print(f"Номер на поръчката: {self.order_id}, "
              f"Статус: {status}, Продукти: ")
        for item in self.items:
            print(f"{item}", end= " ")

orders_list = []
while True:
    print()
    print("---------------------")
    print("        MENU         ")
    print("---------------------")
    print("1.Създаване на поръчка")
    print("2.Добавяне на продукт към поръчката")
    print("3.Завършване на поръчката")
    print("4.Всички поръчки")
    print("0.Изход")
    choice = int(input("Въведете своя избор: "))

    if choice == 1:
        order_id = input("Въведете ID-то на поръчката: ")
        order = Order(order_id)
        orders_list.append(order)

    elif choice == 2:
        order_id = input("Въведете ID-то на поръчката, към което искате да добавите продукт: ")
        item = input("Добавете продукт към поръчката: ")
        for p in orders_list:
            if p.order_id == order_id:
                p.add_items(item)
            else:
                print("Няма поръчка с такова ID!")

    elif choice == 3:
        order_id = input("Въведете ID-то на поръчката, която искате да звършите: ")
        for p in orders_list:
            if p.order_id == order_id:
                p.complete()

    elif choice == 4:
        for p in orders_list:
            p.info()

    elif choice == 0:
        print("Довиждане!")
        break