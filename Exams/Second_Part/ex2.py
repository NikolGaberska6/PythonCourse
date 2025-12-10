class Market:
    def __init__(self, barcode, name, manufacturer, price, quantity):
        self.barcode = barcode
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"{self.name} {self.barcode} {self.price} {self.quantity}"

    def sale(self, quantity):
        if quantity < self.quantity:
            self.quantity -= quantity
        else:
            print(print(f"Няма достатъчно количество от продукта {self.name}"))

    def discount(self):
        if 30 <= self.price <= 50:
            discount = self.price * 0.5
            self.price = self.price - discount
        elif 10 <= self.price <= 30:
            discount = self.price * 0.7
            self.price = self.price - discount
        elif self.price < 10 or self.price > 50:
            self.price = self.price

product_list = []
n = int(input("Моля въведете брой продукти: "))

for i in range(n):

    barcode_input = input("Баркод: ")
    name_input = input("Име: ")
    manufacturer_input = input("Производител: ")
    price_input = float(input("Цена: "))
    quantity_input = int(input("Количество: "))

    product = Market(barcode_input, name_input, manufacturer_input, price_input, quantity_input)
    info = product.info()
    product_list.append(info)
print(product_list)



