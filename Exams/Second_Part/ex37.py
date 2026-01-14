class HotelRoom:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.is_occupied = False
        self.price_per_night = price_per_night

    def room_summary(self):
        if self.is_occupied:
            status = "Заета"
        else:
            status = "Свободна"
        print(f"Стая №: {self.room_number}({self.room_type}), "
              f"Цена: {self.price_per_night} лв. - {status}.")

    def book_room(self):
        if self.is_occupied:
            print("Тази стая в момента е заета!")
            print("Неуспешна резервация!")
        else:
         self.is_occupied = True
         print("Успешна резервация!")
         print("Променихте статуса на стаята!")

    def release_room(self):
        if not self.is_occupied:
            print("Тази стая вече е свободна!")
        else:
           self.is_occupied = False
           print("Освободихте стаята!")
           print("Променихте нейния статус!")

def find_free_rooms(hotel_inventory):
    list_of_free_rooms = []
    for room in hotel_inventory:
        if not room.is_occupied:
            list_of_free_rooms.append(room)
    if len(list_of_free_rooms) > 0:
        print("----Свободни стаи в момента----")
        for room in list_of_free_rooms:
            room.room_summary()
    else:
        print("Няма свободни стаи в момента!")

def calculate_revenue(hotel_inventory):
    occupied_rooms = 0
    total_price = 0
    for room in hotel_inventory:
        if room.is_occupied:
            occupied_rooms += 1
            total_price += room.price_per_night
    if occupied_rooms != 0:
        print(f"Общата потенциална печалба от всички заети стаи за една нощ е: {total_price:.2f} лв.")
    else:
        print("Няма заети стаи в хотела!")

def change_price_by_type(hotel_inventory, target_type, new_price):
    rooms_from_target_type = 0
    for room in hotel_inventory:
        if room.room_type == target_type:
            rooms_from_target_type += 1
            room.price_per_night = new_price
            print("Обновихте цената на стаята!")
    if rooms_from_target_type == 0:
        print("Няма стаи от посочения тип в хотела!")

def main():
    hotel_inventory = []
    n = int(input("Въвдете броя на стаите, които искате да добавите: "))
    for i in range(n):
      print("-----Добавяне на стая в списъка-----")
      room_number = int(input("Моля въведете номера на стаята: "))
      room_type = input("Моля въведете типа на стаята: ")
      price_per_night = float(input("Моля въведете цената на ношувка: "))
      room = HotelRoom(room_number, room_type, price_per_night)
      hotel_inventory.append(room)
      print("Успешно добавихте стаята в списъка!")


    found = False
    room_number = int(input("Въведете номера на стаята, която искате да запазите: "))
    for room in hotel_inventory:
        if room.room_number == room_number:
            found = True
            room.book_room()
    if not found:
        print("Няма стая с посочения номер в хотела!")

    found = False
    room_number = int(input("Въведете номера на стаята, която искате да освободите: "))
    for room in hotel_inventory:
        if room.room_number == room_number:
            found = True
            room.release_room()
    if not found:
        print("Няма стая с посочения номер в хотела!")

    find_free_rooms(hotel_inventory)

    calculate_revenue(hotel_inventory)


    target_type = input("Въведете типа на стаята, иято цена искате да обновите: ")
    new_price = float(input("Въведете новата цена на стаята: "))
    change_price_by_type(hotel_inventory, target_type, new_price)

main()




