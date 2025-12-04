class Taxi:
    def __init__(self, number, driver_name, rate_per_km):
        self.number = number
        self.driver_name = driver_name
        self.is_free = True
        self.rate_per_km = rate_per_km

    def start_ride(self, km):
        if self.is_free:
            course_price = km * self.rate_per_km
            self.is_free = False
            print(f"Цената на курса: {course_price} лв.")
        else:
            print(f"Таксито с номер: {self.number} вече е заето!")

    def finish_ride(self):
        if not self.is_free:
            self.is_free = True
            print(f"Таксито с номер {self.number} е свободно!")
        else:
            print(f"Tаксито с номер {self.number} не е заето!")

    def info(self):
        if self.is_free:
            status = "свободно"
        else:
            status = "заето"
        print(f"Номер на таксито: {self.number} "
              f"Име на шофьора: {self.driver_name} "
              f"Статус: {status} ")
taxi_list = []
while True:
    print("------------------")
    print("        MENU      ")
    print("------------------")
    print("1.Добавяне на такси")
    print("2.Започване на курс")
    print("3.Приключване на курс")
    print("4.Всички таксита")
    print("5.Изход")
    choice = int(input("Изберете: "))

    if choice == 1:
        number = input("Номера на таксито: ")
        driver_name = input("Името на шофьора: ")
        rate_per_km = int(input("Цена на километър: "))
        taxi = Taxi(number, driver_name, rate_per_km)
        taxi_list.append(taxi)
    elif choice == 2:
        number = input("Номера на таксито, което искате да вземете: ")
        km = int(input("Колко километра ще преминете: "))
        for t in taxi_list:
            if t.number == number:
                t.start_ride(km)
    elif choice == 3:
        number = input("Въведете номера на таксито, което искате да освободите: ")
        for t in taxi_list:
            if t.number == number:
                t.finish_ride()
    elif choice == 4:
        for t in taxi_list:
            t.info()
    elif choice == 5:
        print("Довиждане!")
        break