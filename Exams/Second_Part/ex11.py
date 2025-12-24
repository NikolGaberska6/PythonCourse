class Car:
    def __init__(self, vin, brand, model, price, quantity):
        self.vin = vin
        self.brand = brand
        self.model = model
        self.price = price
        self.quantity = quantity

    def sell(self, count):
        if self.quantity >= count:
            self.quantity -= count
            print(f"Успешно продадохте {count} автомобили.")
            print(f"Останало количество: {self.quantity}")
        else:
            print("Недостатъчно количество!")
            print("Неуспешна продажба!")

    def discount(self):
        if self.price > 50000:
            discount = 0.08 * self.price
            print("Отстъпката е 8% от цената.")
            self.price -= discount
            print(f"Новата цена с отстъпката е: {self.price} лв.")
        elif 20000 <= self.price <= 50000:
            discount = 0.05 * self.price
            print("Остъпката е 5% от цената.")
            self.price -= discount
            print(f"Новата цена с отстъпката е: {self.price} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената е: {self.price} лв.")

    def info(self):
        print("------Цялата информация за колата-----")
        print(f"Номер на шаси: {self.vin}, Марка: {self.brand}, Модел: {self.model}, "
              f"Цена: {self.price}, Бройки: {self.quantity}.")

def search_by_vin(car_list, vin):
   for car in car_list:
       if car.vin == vin:
           print("Found!")
           car.info()
           return
   print("Not Found!")

def search_by_brand(car_list, brand):
    cars_of_brand = []
    for car in car_list:
        if car.brand == brand:
            cars_of_brand.append(car)

    sum_of_prices = 0
    average = 0
    for car in cars_of_brand:
        sum_of_prices += car.price

    if len(cars_of_brand) > 0:
      average = sum_of_prices/len(cars_of_brand) #средна цена за марката
    else:
        print("Няма коли на посочената марка!")

    result = []
    for car in cars_of_brand:
        if car.price <= average:
            result.append(car)

    if len(result) > 0:
       print(f"------Коли с цена ≤ средната за марката {average} лв.-------")
       for car in result:
          car.info()
    else:
        print("Няма коли с цена ≤ средната за марката")

def sort_by_price(car_list):
    car_list.sort(key=lambda c: c.price)
    print("Сортирахте по цена във възходящ ред")

def delete_by_model(car_list, model):
    for car in car_list.copy():
        if car.model == model and car.quantity <= 1:
            print(f"Успешно изтрихте {car.model} от листа!")
            car_list.remove(car)

#-----------------ОСНОВНА ПРОГРАМА---------------
car_list = []
n = int(input("Въведете броя на автомобилите, които ще добавите: "))
for i in range(n):
    print("---------Добавяне на автомобил-------")
    vin = input("Номер на шаси: ")
    brand = input("Марка: ")
    model = input("Модел: ")
    price = float(input("Цена: "))
    quantity = int(input("Бройки: "))
    car = Car(vin, brand, model, price, quantity)
    car_list.append(car)
    print("Успешно добавихте колата в листа!")

vin = input("Въведете VIN на автомобила за продажба: ")
count = int(input("Въведете брой за продажба: "))
for car in car_list:
    if car.vin == vin:
        car.sell(count)
        break
else:
    print("Няма автомобил с такъв номер!")

vin = input("Въведете номер на шаси, по който търсите: ")
search_by_vin(car_list, vin)

brand = input("Въведете марката, по която търсите: ")
search_by_brand(car_list, brand)

sort_by_price(car_list)

model = input("Въведете модел на колата, която искате да изтриете: ")
delete_by_model(car_list, model)

