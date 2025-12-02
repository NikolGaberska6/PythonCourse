class Room:
    def __init__(self, number, beds, price_per_night, is_free):
        self.number = number
        self.beds = beds
        self.price_per_night = price_per_night
        self.is_free = is_free

    def book(self):
        if self.is_free:
            self.is_free = False
            print("Стаята е успешно резервирана!")
        else:
            print("Стаята вече е заета!")

    def free(self):
        if not self.is_free:
            self.is_free = True
            print("Освободихте стаята!")
        else:
            print("Стаята е свободна!")


    def info(self):
        if self.is_free:
           status = "свободна"
        else:
            status = "заета"
        print(f"Стая номер: {self.number} с {self.beds} легла,"
              f"струваща {self.price_per_night} на вечер, е {status}")

class Hotel:
    def __init__(self):
     self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
        print(f"Добавихте {room.number} към списъка със стаите!")

    def free_rooms(self):
        for r in self.rooms:
            if r.is_free == is_free:
                print(r.number)

    def book_room(self, number):
        for r in self.rooms:
            if r.number == number:
                r.book()

    def most_expensive_room(self):
        most_expensive = self.rooms[0]
        for r in self.rooms:
            if r.price > most_expensive.price:
                most_expensive = r
                print(f"Най-скъпата стая е: {most_expensive.number}")

    def free_the_room(self, number):
        for r in self.rooms:
            if r.number == number:
                r.free()

    def prices(self):
        for r in self.rooms:
          print(f"Цената на {r.number} стая е: {r.price}")

    def info(self):
        for r in self.rooms:
            r.info()

hotel = Hotel()
def menu():
    print("1.Добавяне на стаи")
    print("2.Извеждане на всички стаи")
    print("3.Резервация")
    print("4.Освобождаване")
    print("5.Цени")
    print("6.Изход")


while True:
    menu()
    choice = int(input("Изберете опция: "))
    if choice == 1:
        number = int(input("Въведете номер на стаята: "))
        beds = int(input("Въведете леглата в стаята: "))
        price_per_night = float(input("Въведете цената за нощувка за 1 вечер: "))
        is_free = input("Въведете дали е заета стаята: (True/False): ").lower()
        room = Room(number, beds, price_per_night, is_free)
        hotel.add_room(room)

    elif choice == 2:
        hotel.info()

    elif choice == 3:
        number = int(input("Номера на стаята, която искате да резервирате: "))
        hotel.book_room(number)

    elif choice == 4:
        number = int(input("Въведете номера на стаята, която искате да освободите: "))
        hotel.free_the_room(number)

    elif choice == 5:
        hotel.prices()

    elif choice == 6:
        print("Довиждане")
        break

