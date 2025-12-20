class Ticket:
    def __init__(self, ticket_num, movie_name, seat, price, status):
        self.ticket_num = ticket_num
        self.movie_name = movie_name
        self.seat = seat
        self.price = price
        self.status = status

    def show_ticket(self):
        print("Цялата информация за билета: ")
        print(f"Номер на билета: {self.ticket_num}, "
              f"Име на филма: {self.movie_name}, Номер на място: {self.seat},"
              f"Цена: {self.price}, Статус: {self.status}.")

    def change_seat(self):
        new_seat = int(input("Въвдете новия номер на мястото: "))
        self.seat = new_seat
        print("Успешно променихте номера на мястото!")

tickets_list = []
def input_ticket():
   print("----------Добавяне на билет-------")
   ticket_num = int(input("Номер на билета: "))
   movie_name = input("Име на филма: ")
   seat = int(input("Номер на място: "))
   price = float(input("Цена на билета: "))
   status = input("Статус на мястото (заето/свободно): ")
   return Ticket(ticket_num, movie_name, seat, price, status)

def find_ticket(tickets_list, ticket_num):
    for ticket in tickets_list:
        if ticket.ticket_num == ticket_num:
            print("Found!")
            print(f"Статус: {ticket.status}")
            return
    print("Not Found!")

def add_ticket(tickets_list, new_ticket):
    tickets_list.append(new_ticket)
    print("Успешно доавихте билета към листа!")

#--------------ОСНОВНА ПРОГРАМА--------------
def main():
  n = int(input("Броя на билетите, които ще запазвате: "))
  for i in range(n):
      new_ticket = input_ticket()
      add_ticket(tickets_list, new_ticket)

  ticket_num = int(input("Въведете номера, по който търсите: "))
  find_ticket(tickets_list, ticket_num)

  new_ticket = input_ticket()
  add_ticket(tickets_list, new_ticket)

main()