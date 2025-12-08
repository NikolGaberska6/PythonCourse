class Clothing:
    def __init__(self, barcode, name, price, quantity):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.quantity = quantity

    def sale(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
            print(f"Намалихте количеството на {self.name} с {qty}")
            print(f"Новото количество е: {self.quantity}")
        else:
            print("Грешка! Недостатъчно количество!")

    def info(self):
        return f"Баркод: {self.barcode}, Име: {self.name}, Цена: {self.price}, Количество: {self.quantity}"


class SummerClothing(Clothing):
    def __init__(self, barcode, name, price, quantity, material):
        super().__init__(barcode, name, price, quantity)
        self.material = material

    def info(self):
        info_text = super().info() + f", Материал {self.material}"
        if self.material == "synthetic":
            info_text += "⚠️(Синтетичен материал!)"
        return info_text

class WinterClothing(Clothing):
    def __init__(self, barcode, name, price, quantity, temperature_rating):
        super().__init__(barcode, name, price, quantity)
        self.temperature_rating = temperature_rating

    def info(self):
        info_text = super().info() + f", Температурен рейтинг: {self.temperature_rating}°C"
        if self.temperature_rating < -10:
            info_text += "⚠️(Много студоустойчиво!)"
        return info_text

#Функция, която показва всички продукти със специални предупреждения.
def warnings(product_list):
    for product in product_list:
        text = product.info()
        if "⚠️" in text:
            print(text)

products_list = [
    SummerClothing("1001", "Тениска", 25, 10, "cotton"),
    SummerClothing("1002", "Потник", 15, 5, "synthetic"),
    WinterClothing("2001", "Яке", 180, 3, -20),
    WinterClothing("2002", "Пуловер", 60, 8, -5)
]

for p in products_list:
    p.info()

products_list[0].sale(3)
products_list[1].sale(4)

