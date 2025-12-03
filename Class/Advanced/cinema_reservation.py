class Seat:
    def __init__(self, number):
        self.number = number
        self.is_free = True

    def reserve(self):
        if self.is_free:
            print(f"Заехте място с номер: {self.number}!")
            self.is_free = False
        else:
            print("Това място вече е заето!")

    def cancel(self):
        if not self.is_free:
            print("Отказахте резервацията си!")
            print(f"Освободихте място с номер {self.number}")

    def free_seats(self):
        if self.is_free:
            print(f"{self.number}")

    def booked_seats(self):
        if not self.is_free:
            print(f"{self.number}")


    def info(self):
        if self.is_free:
            status = "свободно"
        else:
            status = "заето"
        print(f"Номер на място: {self.number}"
              f"Статус на място: {status}")


cinema_seats = []
while True:
  print("1.Добавяне на място в списъка")
  print("2.Резервиране на място")
  print("3.Отказване на резервация")
  print("4.Показване на свободните места")
  print("5.Показване само на заетите места")
  print("0.Изход")
  choice = int(input("Изберете опция: "))

  if choice == 1:
      number = int(input("Въведете мястото, което искате да добавите: "))
      seat = Seat(number)
      cinema_seats.append(seat)

  elif choice == 2:
      number = int(input("Въведете мястото, което искате да резервирате: "))
      for s in cinema_seats:
          if s.number == number:
              s.reserve()

  elif choice == 3:
      number = int(input("Въведете мястото, което искате да освободите: "))
      for s in cinema_seats:
          if s.number == number:
              s.cancel()

  elif choice == 4:
      print("Номерата на свободните стаи са: ")
      for s in cinema_seats:
          s.free_seats()

  elif choice == 5:
      print("Номерата на заетите стаи са: ")
      for s in cinema_seats:
          s.booked_seats()

  elif choice == 0:
      print("Довиждане")
      break
