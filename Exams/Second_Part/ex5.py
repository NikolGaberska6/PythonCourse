class ParcelDelivery:
    def __init__(self, tracking_number, recipient_name, weight,
                 delivery_date, delivery_status):
        self.tracking_number = tracking_number
        self.recipient_name = recipient_name
        self.weight = weight
        self.delivery_date = delivery_date
        self.delivery_status = delivery_status

    def show_info(self):
        print(f"Номер за проследяване: {self.tracking_number}, "
              f"Име на получател: {self.recipient_name}, "
              f"Тегло: {self.weight}, Дата на доставка: {self.delivery_date}, "
              f"Статус на доставка: {self.delivery_status}")

    def update_weight(self, new_weight):
        self.weight = new_weight
        print(f"Променихте теглото на пратката на {new_weight} кг.")

def input_parcel():
    tracking_number = input("Въведете номер на проследяване: ")
    recipient_name = input("Въведете име на получател: ")
    weight = int(input("Въведете тегло в килограми: "))
    delivery_date = input("Въвдете дата за доставка: ")
    delivery_status = input("Въведете статус на доставката: ")
    return ParcelDelivery(tracking_number, recipient_name, weight, delivery_date, delivery_status)

def check_status(parcels_list, tracking_number):
    for parcel in parcels_list:
        if parcel.tracking_number == tracking_number:
            print(f"Статуса на поръчката е: {parcel.delivery_status}")
            return
    print("Not Found!")

def add_parcel(parcels_list, new_parcel):
    parcels_list.append(new_parcel)
    print("Успешно добавена поръчка!")

def main():
   parcels_list = []
   n = int(input("Въведете колко продкти ще добавяте: "))
   for i in range(n):
     parcel = input_parcel()
     add_parcel(parcels_list, parcel)

   tracking_number = input("Въведете номер, по който ще проверявате: ")
   check_status(parcels_list, tracking_number)

   print("--------Добавяне на поръчка-------")
   new_parcel = input_parcel()
   add_parcel(parcels_list, new_parcel)

main()