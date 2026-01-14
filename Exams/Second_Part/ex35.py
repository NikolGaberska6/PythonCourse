class Car:
    def __init__(self, brand, model, year, price, is_available):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.is_available = is_available

    def display_car(self):
        print("------Цялата информация за автомобила----")
        print(f"Марка: {self.brand}, Модел: {self.model}, Година: {self.year}, "
              f"Цена: {self.price}, Наличност: {self.is_available}.")

    def apply_discount(self, percent):
        print(f"Отстъпката е {percent}% от цената!")
        discount = percent/100 * self.price
        self.price -= discount
        print(f"Новата цена на автомобила с отстъпката е: {self.price:.2f} лв.")

def search_by_brand(car_inventory, brand_name):
    all_cars_from_brand = []
    for car in car_inventory:
        if car.brand.lower() == brand_name.lower():
            all_cars_from_brand.append(car)
    if len(all_cars_from_brand) > 0:
        print("-----Информация за всички коли от посочената марка-----")
        for car in all_cars_from_brand:
            car.display_car()
    else:
        print("Brand not available!")

def calculate_total_value(car_inventory):
    total_value = 0
    for car in car_inventory:
        if car.is_available:
            total_value += car.price
    if total_value != 0:
        print(f"Общата стойност на всички налични автомобили е: {total_value:.2f} лв.")
    else:
        print("Няма налични автомобили в списъка!")

def main():
    car_inventory = []
    n = int(input("Въведете броя на колите, които искате да добавите: "))
    for i in range(n):
        brand = input("Въведете марката на колата, която искате да добавите: ")
        model = input("Въведете модела на колата, която искате да добавите: ")
        year = int(input("Въведете година на производство на колата, която искате да добавите: "))
        price = float(input("Въведете цената на колата, която искате да добавите: "))
        available = input("Наличност на автомобила (да/не): ")
        if available.lower() == "да":
            is_available = True
        else:
            is_available = False
        car = Car(brand, model, year, price, is_available)
        car_inventory.append(car)
        print("Успешно добавихте колата към списъка!")

    found = False
    model = input("Въведете модела на колата, която искате да намалите: ")
    for car in car_inventory:
        if car.model.lower() == model.lower():
            found = True
            percent = int(input("Въведете процента на отстъпката (цяло число): "))
            car.apply_discount(percent)
    if not found:
        print("Няма кола с посочения модел в списъка с коли!")

    brand_name = input("Въведете марката на колата, която търсите: ")
    search_by_brand(car_inventory, brand_name)

    calculate_total_value(car_inventory)

main()