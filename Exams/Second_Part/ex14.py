class HotelRoom:
    def __init__(self, room_number, type, price_per_night, capacity, available_rooms):
        self.room_number = room_number
        self.type = type
        self.price_per_night = price_per_night
        self.capacity = capacity
        self.available_rooms = available_rooms

    def book(self, rooms):
        if rooms <= self.available_rooms:
            print(f"Резервирахте {rooms} на брой стаи.")
            self.available_rooms -= rooms
            print(f"Свободните стаи са: {self.available_rooms}")
        else:
            print("Недостатъчно свободни стаи за резвервация!")

    def discount(self):
        if 80 < self.price_per_night <= 150:
            discount = 0.05 * self.price_per_night
            print("Отстъпката е 5% от цената!")
            self.price_per_night -= discount
            print(f"Новата цена на стаята за нощувка с отстъпката "
                  f"е: {self.price_per_night} лв.")
        elif 50 <= self.price_per_night <= 80:
            discount = 0.08 * self.price_per_night
            print("Отстъпката е 8% от цената!")
            self.price_per_night -= discount
            print(f"Новата цена на стаята за нощувка с отстъпката "
                  f"е: {self.price_per_night} лв.")
        else:
            print("Няма отстъпка!")
            print("Цената на стаята за нощувка без отстъпка "
                  f"е: {self.price_per_night} лв")

    def info(self):
        print(f"Номер на стаята: {self.room_number}, Тип: {self.type}, "
              f"Цена за една нощувка: {self.price_per_night}, Капацитет: {self.capacity},"
              f"Свободни стаи от същия тип: {self.available_rooms}.")


def search_by_room_number(room_list, room_number):
    for room in room_list:
        if room.room_number == room_number:
            print(f"Стаята с номер '{room_number}' е намерена в списъка със стаи!")
            return
    print(f"Няма стая с номер '{room_number}' в листа!")

def search_by_type(room_list, type):
    rooms_of_that_type = []
    for room in room_list:
        if room.type == type:
            rooms_of_that_type.append(room)

    average = 0
    sum_of_room_prices = 0
    if len(rooms_of_that_type) > 0:
        for room in rooms_of_that_type:
            sum_of_room_prices += room.price_per_night
        average = sum_of_room_prices / len(rooms_of_that_type)
        print(f"Средната цена за дадения тип на стаята е: {average} лв.")
    else:
        print("Няма стаи в списъка от посочения тип!")

    result = []
    for room in rooms_of_that_type:
        if room.price_per_night <= average:
            result.append(room)

    if len(result) > 0:
        print("Стаите в списъка от посочения тип с цена ≤ средната за типа са: ")
        for room in result:
            room.info()
    else:
        print("Няма стаи в списъка от посочения тип цена ≤ средната за типа!")


def sort_by_available_rooms(room_list):
    room_list.sort(key=lambda r: r.available_rooms)
    print("Сортирахте листа във възходящ ред!")

def delete_by_type(room_list, type):
    for room in room_list.copy():
        if room.type == type:
            if room.available_rooms <= 2:
                print(f"Изтрихте стаята от типа {type} от списъка.")
                room_list.remove(room)

def main():
    room_list = []
    n = int(input("Въведете колко на брой стаи ще добавите: "))
    for i in range(n):
        room_number = int(input("Въведете номер на стаята: "))
        type = input("Въведете типа на стаята (single, double, suit): ")
        price_per_night = float(input("Въведете цена за една вечер на стаята: "))
        capacity = int(input("Въведете капацитета на стаята (колко души събира): "))
        available_rooms = int(input("Въведете броя на свободните стаи от същия тип: "))
        room = HotelRoom(room_number, type, price_per_night, capacity, available_rooms)
        room_list.append(room)
        print("Успешно добавихте стаята към списъка със стаи!")

    type = input("Въведете типа на стаите, които искате да резервирате: ")
    for room in room_list:
        if room.type == type:
            rooms = int(input("Въведете колко стаи искате да резервирате: "))
            room.book(rooms)

    room_number = int(input("Въвдете номера на стаята, която търсите: "))
    search_by_room_number(room_list, room_number)

    type = input("Въведете типа на стаята, която търсите: ")
    search_by_type(room_list, type)

    sort_by_available_rooms(room_list)

    type = input("Въведете типа на стаята, която искате да изтриете: ")
    delete_by_type(room_list, type)

main()