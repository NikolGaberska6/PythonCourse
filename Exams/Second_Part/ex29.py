class HotelRoom:
    def __init__(self, number, type, price, is_free, nights):
        self.number = number
        self.type = type
        self.price = price
        self.is_free = is_free
        self.nights = nights

    def book(self, nights):
        if self.is_free == "свободна":
            self.nights += nights
            print(f"Резервирахте стаята с "
                  f"посочения номер за {nights} брой нощувки!")
            self.is_free = "заета"
        else:
            print("Стаята е заета!")
            print("Неуспешна резервация!")

    def total_price(self):
        total = self.nights * self.price
        print(f"Общата цена за престоя е: {total:.2f} лв.")

def free_rooms(rooms):
    free_rooms_list = []
    for room in rooms:
        if room.is_free.lower() == "свободна":
            free_rooms_list.append(room)
    if len(free_rooms_list) > 0:
        print("Свободните стаи: ")
        for room in free_rooms_list:
            print(room.number)
    else:
        print("Няма свободни стаи в списъка!")
    return free_rooms_list

def rooms_below_price(rooms, price):
    rooms_below_price_list = []
    for room in rooms:
        if room.price <= price:
            rooms_below_price_list.append(room)
    if len(rooms_below_price_list) > 0:
        print("Стаите с цена за нощувка по-ниска или равна на зададената: ")
        for room in rooms_below_price_list:
            print(room.number)
    else:
        print("Няма стаи с цена за нощувка по-ниска или равна на зададената!")
    return rooms_below_price_list

def sort_by_price(rooms):
    rooms.sort(key=lambda r: r.price)
    print("Сортирахте стаите по цена във възходящ ред!")
    print("Сортираният лист: ")
    for room in rooms:
        print(room.number)
    return rooms

def delete_unbooked(rooms):
    num_deleted_rooms = 0
    for room in rooms.copy():
        if room.is_free.lower() == "свободна":
            num_deleted_rooms += 1
            print(f"Изтрихте стаята с номер {room.number} от списъка със стаи!")
            rooms.remove(room)
    if num_deleted_rooms != 0:
        print(f"Броя на изтритите стаи е: {num_deleted_rooms}.")
    else:
        print("Няма свободни стаи в списъка със стаи!")

def main():
    rooms = []
    n = int(input("Въведете броя на стаите, които искате да добавите: "))
    for i in range(n):
        number = int(input("Въведете номера на стаята, която искате да добавите: "))
        type = input("Въведете типа на стаята, която искате да добавите: ")
        price = float(input("Въведете цената на стаята, която искате да добавите: "))
        is_free = input("Въведете дали стаята, която искате да добавите е свободна или заета: ")
        nights = int(input("Въведете брой нощувки на стаята, която искате да добавите: "))
        room = HotelRoom(number, type, price, is_free, nights)
        rooms.append(room)
        print("Добавихте стаята в списъка със стаи!")

    found = False
    number = int(input("Въведете номера на стаята, която искате да запазите: "))
    for room  in rooms:
        if room.number == number:
            found = True
            nights = int(input("Въведете брой нощувки, които искате добавите: "))
            room.book(nights)
    if not found:
        print("Няма стая с посочения номер в списъка със стаи!")

    found = False
    number = int(input("Въведете номера на стаята, на която искате общата цена за престоя: "))
    for room in rooms:
        if room.number == number:
            found = True
            room.total_price()
    if not found:
        print("Няма стая с посочения номер в списъка със стаи!")

    free_rooms(rooms)

    price = float(input("Въведете максимална допустима цената на стаята, която искате да запазите: "))
    rooms_below_price(rooms, price)

    sort_by_price(rooms)

    delete_unbooked(rooms)

main()
