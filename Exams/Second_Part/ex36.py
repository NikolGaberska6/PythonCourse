class AutoPart:
    def __init__(self, part_id, name, brand, price, quantity):
        self.part_id = part_id
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("---Подробна информация за авточастта---")
        print(f"Идентификационен номер: {self.part_id}, Име: {self.name}, "
              f"Марка автомобила: {self.brand}, Цена: {self.price}, "
              f"Налично количество: {self.quantity}.")

    def update_price(self, new_price):
        print("Промяна на цената на частта!")
        self.price = new_price
        print("Цената е променена успешно!")

def part_input():
    print("-----Добавяне на част в списъка-----")
    part_id = input("Въведете идентификационния номер на частта: ")
    name = input("Въведете името на частта: ")
    brand = input("Въведете марка автомобил: ")
    price = float(input("Въведете цена на частта: "))
    quantity = int(input("Въведете налично количество на частта: "))
    return AutoPart(part_id, name, brand, price, quantity)


def find_part(warehouse_stock, search_id):
    for part in warehouse_stock:
        if part.part_id == search_id:
            print("Частта е намерена!")
            part.display_info()
            return
    print("Part not found")

def calculate_total_value(warehouse_stock):
    total_price_for_all = 0
    for part in warehouse_stock:
        price_of_stock = part.price * part.quantity
        total_price_for_all += price_of_stock
    print(f"Общата стойност на всички части в склада е: {total_price_for_all:.2f} лв.")

def add_new_part(warehouse_stock, new_part):
    warehouse_stock.append(new_part)
    print("Успешно добавихте новата част в списъка!")

def main():
    warehouse_stock = []
    n = int(input("Въведете броя на частите, които искате да добавите: "))
    for i in range(n):
        part = part_input()
        warehouse_stock.append(part)
        print("Успешно добавихте новата част в списъка!")

    found = False
    part_id = input("Въведете идентификационния номер, на частта, чиято цена искате да промените: ")
    for part in warehouse_stock:
        if part.part_id == part_id:
            found = True
            new_price = float(input("Въведете новата цена на частта: "))
            part.update_price(new_price)
    if not found:
        print("Не е намерена част с посочения идентификационен номер!")


    search_id = input("Въведете идентификационния номер, по който търсите: ")
    find_part(warehouse_stock, search_id)

    calculate_total_value(warehouse_stock)

    new_part = part_input()
    add_new_part(warehouse_stock, new_part)

main()

