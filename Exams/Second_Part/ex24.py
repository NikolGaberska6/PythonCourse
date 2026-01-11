import sys
class ClothesShop:
    def __init__(self, clothes_type, brand, price, quantity, size):
        self.clothes_type = clothes_type
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.size = size

    def sale(self, q):
        if self.quantity >= q:
            self.quantity -= q
            print(f"Продадохте {q} артикула!")
        else:
            print("Нямате достатъчно артикули!")

    def discount(self):
        if 1 <= self.quantity <= 3:
            discount = 0.35
            print("Отстъпката е 35% от цената!")
            discount_price = 0.35 * self.price
            self.price -= discount_price
            print(f"Новата цена с отстъпката е: {self.price}")
        elif 4 <= self.quantity <= 6:
            discount = 0.15
            print("Отстъпката е 15% от цената!")
            discount_price = 0.15 * self.price
            self.price -= discount_price
            print(f"Новата цена с отстъпката е: {self.price}")
        else:
            print("Няма отстъпка")

clothes_list = []
k = int(input("Въведете брой продукти: "))
for i in range(k):
    clothes_type = input("Въведи тип дреха: ")
    brand = input("Въведи бранд на дрехата: ")
    price = float(input("Въведи цена на дрехата: "))
    quantity = int(input("Въведи количество на дрехата: "))
    size = int(input("Въведете размер на дрехата: "))
    clothes = ClothesShop(clothes_type, brand, price, quantity, size) #инстанция на класа
    clothes_list.append(clothes)

def search_by_size_type(clothes_list, size, type):
    new_clothes_list =[]
    for clothes in clothes_list:
        if clothes.size == size and clothes.type == type:
            new_clothes_list.append(clothes)

    average = 0
    sum_of_clothes = 0
    count_of_clothes = 0
    result = []
    for clothes in new_clothes_list:
        sum_of_clothes += clothes.price
        count_of_clothes += clothes.quantity
    average = sum_of_clothes/count_of_clothes

    for clothes in new_clothes_list:
        if clothes.price < average:
          result.append(clothes)
     return result

def cheapest_clothes(clothes_list, brand):
    brand_list = []
    for clothes in clothes_list:
        if clothes.brand == brand:
            brand_list.append(clothes)

    min_price = sys.maxsize
    for clothes in brand_list:
        if clothes.price < min_price:
            min_price = clothes.price
    print(f"Минималната цена на дадената марка е: {min_price}")

    if len(brand_list) == 0:
        print("brand is not available")

    for clothes in clothes_list:
        print(clothes.brand)

def sort_clothes(clothes_list):
    clothes_list.sort(key=lambda a: a.price, reverse=True)
    print("Сортирахте списъка в низходящ ред по цена!")

def delete_by_type(clothes_list, type):
    for clothes in clothes_list:
        if clothes.type == type:
            if clothes.quantity < 2:
                clothes_list.remove(clothes)