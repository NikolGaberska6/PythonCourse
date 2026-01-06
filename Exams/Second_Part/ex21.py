class Car:
    def __init__(self, brand, model, year, price, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def drive(self, km):
        self.mileage += km
        print(f"Увеличихте пробега на автомобила с {km} км.")
        print(f"Новия пробег е: {self.mileage} км.")

    def apply_depreciation(self, current_year):
        if current_year - self.year > 5:
            print("Цената на автомобила се намалява с 5%.")
            self.price -= self.price * 0.05
            print(f"Новата цена на автомобила е: {self.price}")

    def info(self):
        print(f"Марка: {self.brand}, Модел: {self.model}, "
              f"Година на производство: {self.year}, Цена: {self.price}, Пробег: {self.mileage}.")

def search_by_brand(cars, brand):
    cars_from_brand = []
    for car in cars:
        if car.brand == brand:
            cars_from_brand.append(car)
    if len(cars_from_brand) > 0:
        print("Намерихте коли в списъка на посочената марка!")
        for car in cars_from_brand:
            car.info()
    else:
        print("Няма коли в списъка на посочената марка!")

def average_price(cars):
    average_price = 0
    sum_of_prices = 0
    for car in cars:
        sum_of_prices += car.price
    average_price = sum_of_prices / len(cars)
    print(f"Средната цена на всички автомобили е: {average_price:.2f} лв.")
    return average_price

def sort_by_year(cars):
    cars.sort(key=lambda c: c.year)
    print("Сортирахте автомобилите по година на производство във възходящ ред!")
    return cars

def delete_old_cars(cars, year):
    for car in cars.copy():
        if car.year < year:
            print("Изтрихте колата от списъка с коли!")
            cars.remove(car)

def main():
    cars = []
    n = int(input("Въведете броя на колите, които искате да добавите: "))
    for i in range(n):
        brand = input("Въведете марката на колата, която искате да добавите: ")
        model = input("Въведете модела на колата, която искате да добавите: ")
        year = int(input("Въведете година на производство на колата, която искате да добавите: "))
        price = float(input("Въведете цена на колата, която искате да добавите: "))
        mileage = int(input("Въведете километрите на колата, която искате да добавите: "))
        car = Car(brand, model, year, price, mileage)
        cars.append(car)
        print("Успешно добавихте колата към списъка с коли!")

    found = False
    model = input("Въведете модела на колата, към която искате да добавите пробег: ")
    for car in cars:
        if car.model == model:
            found = True
            print("Намерихме кола с посочения модел в списъка!")
            km = int(input("Въведете колко километра искате да добавите: "))
            car.drive(km)
    if not found:
        print("Не намерихме кола с посочения модел в списъка!")

    found = False
    model = input("Въведете модела на колата, към която искате да проверите за отстъпка: ")
    for car in cars:
        if car.model == model:
            found = True
            print("Намерихме кола с посочения модел в списъка!")
            year = int(input("Въведете сегашната годината: "))
            car.apply_depreciation(year)
    if not found:
        print("Не намерихме кола с посочения модел в списъка!")

    brand = input("Въведете марката на колата, която търсите: ")
    search_by_brand(cars, brand)

    average_price(cars)

    sort_by_year(cars)

    year = int(input("Въведете година, с която искате да сравнявате: "))
    delete_old_cars(cars, year)

main()