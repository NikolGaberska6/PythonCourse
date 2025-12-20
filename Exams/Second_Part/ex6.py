class MovieTicket:
    def __init__(self, ticket_id, movie_name, seat_number, price, status):
        self.ticket_id = ticket_id
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price
        self.status = status

    def ticket_info(self):
        print(f"ИД на билета: {self.ticket_id}, Име на филма: {self.movie_name}, "
              f"Номер на място: {self.seat_number}, Цена: {self.price}, "
              f"Статус: {self.status}.")

    def change_seat(self):
        new_seat_number = int(input("Въведете нов номер на място: "))
        self.seat_number = new_seat_number
        print("Променихте номера на мястото!")
        print(f"Новият номер е: {self.seat_number}")

tickets_list = []
def input_ticket():
    print("--------Закупуване на билет----------")
    ticket_id = input("ИД на билета: ")
    movie_name = input("Име на филма: ")
    seat_number = int(input("Номер на място: "))
    price = float(input("Цена: "))
    status = input("Статус (купена, отменена, резервирана): ")
    return MovieTicket(ticket_id, movie_name, seat_number, price, status)

def find_ticket(tickets_list, ticket_id):
    for ticket in tickets_list:
        if ticket.ticket_id == ticket_id:
            print("Found!")
            print(ticket.status)
            return
    print("Not Found")

def add_ticket(tickets_list, new_ticket):
    tickets_list.append(new_ticket)
    print("Успешно добавен билет!")

#----------ОСНОВНА ПРОГРАМА---------------
def main():
   n = int(input("Въвдете колко билета ще закупите: "))
   for i in range(n):
      new_ticket = input_ticket()
      add_ticket(tickets_list, new_ticket)

   ticket_id = input("ИД на билета, който търсите: ")
   find_ticket(tickets_list, ticket_id)

   new_ticket = input_ticket()
   add_ticket(tickets_list, new_ticket)

main()