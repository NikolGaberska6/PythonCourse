class Product:
    def __init__(self, id, name, category, price, quantity):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def sell(self, n):
        if self.quantity >= n:
            print(f"Продадохте {n} броя от посочения продукт!")
            self.quantity -= n
            print(f"Новото количество на продукта е: {self.quantity}")
        else:
            print("Недостатъчно количество!")
            print("Неуспешна продажба!")

    def apply_discount(self):
        if self.quantity > 50:
            discount = 0.15 * self.price
            print("Отстъпката е 15% от цената!")
            self.price -= discount
            print(f"Новата цена на продукта с отстъпката е: {self.price} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената на продукта без отстъпка е: {self.price} лв.")

    def info(self):
        print(f"ИД: {self.id}, Име: {self.name}, Категория: {self.category}, "
              f"Цена: {self.price}, Количество: {self.quantity}.")


def search_by_category(products, category):
    product_by_category = []
    for product in products:
        if product.category == category:
            product_by_category.append(product)
    if len(product_by_category) > 0:
        print("Всички продукти от посочената категория: ")
        for product in product_by_category:
            product.info()
    else:
        print("Няма продукти от посочената категория в списъка с продукти!")

def low_stock(products):
    low_stock_products = []
    for product in products:
        if product.quantity <= 5:
            low_stock_products.append(product)
    if len(low_stock_products) > 0:
        for product in products:
            product.info()
    else:
        print("Няма продукти в листа с наличност на продукта <= 5!")

    return low_stock_products

def sort_by_price(products):
    products.sort(key=lambda p: p.price)
    print("Сортирахте списъка във възходящ ред по цена!")
    print("Новият списък е: ")
    for product in products:
        product.info()

def delete_zero_quantity(products):
    for product in products.copy():
        if product.quantity == 0:
            print(f"Изтрихте продукта {product.name} от списъка с продукти!")
            products.remove(product)

def main():
    products = []
    n = int(input("Въведете броя на продуктите, които искате да добавите: "))
    for i in range(n):
        id = input("Въведете ID-то на продукта, който искате да добавите: ")
        name = input("Въведете името на продукта, който искате да добавите: ")
        category = input("Въведете категорията на продукта, който искате да добавите: ")
        price = float(input("Въведете цената на продукта, който искате да добавите: "))
        quantity = int(input("Въведете наличността на продукта, който искате да добавите: "))
        product = Product(id, name, category, price, quantity)
        products.append(product)
        print("Успешно добавихте продукта в списъка!")

    found = False
    id = input("Въведете ID-то на продукта, който искате да продавате: ")
    for product in products:
        if product.id == id:
            found = True
            n = int(input("Въвдете количеството от продукта, което искате да продадете: "))
            product.sell(n)
    if not found:
        print("Не намерихме продукт с посоченото ID в списъка с продукти!")

    found = False
    id = input("Въведете ID-то на продукта, който искате да проверите за отстъпка: ")
    for product in products:
        if product.id == id:
            found = True
            product.apply_discount()
    if not found:
        print("Не намерихме продукт с посоченото ID в списъка с продукти!")

    category = input("Въведете категорията по която търсите: ")
    search_by_category(products, category)

    low_stock(products)

    sort_by_price(products)

    delete_zero_quantity(products)

main()