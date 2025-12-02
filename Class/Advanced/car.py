class Car:
    def __init__(self, model, brand, year, mileage, fuel):
        self.model = model
        self.brand = brand
        self.year = year
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, km):
        if km < 0:
            print("Грешка!")
        else:
            self.mileage += km
            print(f"Пробегът на колата е увеличен с {km} km")
            print(f"Новият пробег е: {self.mileage}")

    def fuel(self, amount):
        if self.fuel <= 100:
         self.fuel += amount
         print(f"Добавихте {amount} литра гориво")
        else:
            print("Достигнахте максимумът литри!")

    def info(self):
        print(f"Информация за автомобила: {self.model}, {self.brand},"
              f" {self.year}, {self.mileage}, {self.fuel}")


class CarFleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Автомобилът е добавен успешно!")

    def find_by_brand(self, brand):
        for car in self.cars:
            if car.brand == brand:
                print(car.info())
                return
            print("Няма коли от марката!")

    def total_mileage(self):
        sum = 0
        for car in self.cars:
            sum += car.mileage
        print(f"Общо изминати километри: {sum}")

    def oldest_car(self):
        oldest_car = self.cars[0]
        if len(self.cars) == 0:
            print("Автокъщата е празна")
        else:
            for car in self.cars:
                if car.year < oldest_car.year:
                    oldest_car = car
            print(f"Най-старата кола е: {oldest_car.info()}")

    def show_all_cars(self):
        for car in self.cars:
            car.info()

    def find_car(self, brand, model):
        for car in self.cars:
            if car.brand == brand and car.model == model:
                return car.info

carFleet = CarFleet()

print("\n=== МЕНЮ ===")
print("1. Добави автомобил")
print("2. Покажи всички автомобили")
print("3. Търси автомобили по марка")
print("4. Общо изминати километри в автопарка")
print("5. Най-старият автомобил")
print("6. Управление на автомобил (drive/refuel)")
print("0. Изход")

while True:
    choice = int(input("Избор: "))
    if choice == 1:
        brand = input("Марка: ")
        model = input("Модел: ")
        year = int(input("Година: "))
        mileage = int(input("Пробег: "))
        fuel = int(input("Гориво (0–100): "))
        car = Car(model, brand, year, mileage, fuel)
        carFleet.add_car(car)
    elif choice == 2:
        carFleet.show_all_cars()
    elif choice == 3:
        brand = input("Въведете марката: ")
        carFleet.find_by_brand(brand)
    elif choice == 4:
        carFleet.total_mileage()
    elif choice == 5:
        carFleet.oldest_car()
    elif choice == 6:

        user_choice = input("Изберете между: drive/refuel: ")
        brand = input("Въведете марка на автомобила: ")
        model = input("Въведете модел на автомобила: ")

        if user_choice == "drive":
            selected_car = carFleet.find_car(brand, model)
            km = int(input("Въведете колко километри са изминати: "))
            selected_car.drive(km)
        elif user_choice == "refuel":
            selected_car = carFleet.find_car(brand, model)
            amount = int(input("Въведете колко литра искате да заредите: "))
            selected_car.fuel(amount)

    elif choice == 0:
        break