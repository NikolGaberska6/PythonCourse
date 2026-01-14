class HotelBooking:
    def __init__(self, guest_name, room_number, nights, price_per_night, status):
        self.guest_name = guest_name
        self.room_number = room_number
        self.nights = nights
        self.price_per_night = price_per_night
        self.status = status

    def booking_info(self):
        print("------Пълната информация за резервацията-------")
        print(f"Име на госта: {self.guest_name}, Номер на стаята: {self.room_number}, "
              f"Брой нощувки: {self.nights}, Цена на нощувка: {self.price_per_night}, "
              f"Статус: {self.status}.")
        total_price = self.nights * self.price_per_night
        print(f"Общата сума за престоя е: {total_price:.2f} лв.")

    def update_nights(self):
        new_nights = int(input("Въведете нов брой нощувки: "))
        self.nights = new_nights
        print("Успешно променихте броя на нощувките!")

def input_info():
    print("Моля въведете данните за поръчката!")
    guest_name = input("Въведете името на госта: ")
    room_number = int(input("Въведете номера на стаята: "))
    nights = int(input("Въведете броя на нощувките: "))
    price_per_night = float(input("Въведете цена на нощувка: "))
    status = input("Въведете статус на поръчката (потвърдена, чакаща, анулирана): ")
    return HotelBooking(guest_name, room_number, nights, price_per_night, status)

def find_by_guest(reservation_list, name):
    for reservation in reservation_list:
        if reservation.guest_name == name:
            reservation.booking_info()
            return
    print("No booking found!")

def add_booking(reservation_list, new_booking):
    reservation_list.append(new_booking)
    print("Успешно добавихте резервацията в списъка!")

def main():
    reservation_list = []
    n = int(input("Въведете броя на поръчките, които искате да добавите: "))
    for i in range(n):
        reservation = input_info()
        reservation_list.append(reservation)
        print("Успешно добавихте резервацията към списъка!")

    guest_name = input("Въведете името на госта, чиято резервация искате да промените: ")
    found = False
    for reservation in reservation_list:
        if reservation.guest_name == guest_name:
            found = True
            reservation.update_nights()
    if not found:
        print("Няма име на гост в списъка, което да отговаря на посоченото!")

    name = input("Въведете името на госта, по който търсите резервация: ")
    find_by_guest(reservation_list, name)

    print("---------Добавяне на резервация------")
    new_booking = input_info()
    add_booking(reservation_list, new_booking)

main()