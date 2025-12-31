class Movie:
    def __init__(self, movie_id, title, genre, ticket_price, tickets_available):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.ticket_price = ticket_price
        self.tickets_available = tickets_available

    def sell_tickets(self, count):
        if self.tickets_available >= count:
            print(f"Вие продадохте {count} броя билета.")
            self.tickets_available -= count
            print(f"Новата бройка налични билети е: {self.tickets_available}.")
        else:
            print("Недостатъчно билети! Неуспешна покупка!")

    def discount(self):
        if 12 < self.ticket_price <= 20:
            discount = 0.1 * self.ticket_price
            print("Отстъпката е 10% от цената на билета.")
            self.ticket_price -= discount
            print(f"Новата цена на билета с отстъпката е: {self.ticket_price} лв.")
        elif 8 <= self.ticket_price <= 12:
            discount = 0.15 * self.ticket_price
            print("Отстъпката е 15% от цената на билета.")
            self.ticket_price -= discount
            print(f"Новата цена на билета с отстъпката е: {self.ticket_price} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената без отстъпка е: {self.ticket_price} лв.")

    def info(self):
        print(f"ИД на филма: {self.movie_id}, Име: {self.title}, Жанр: {self.genre}, "
              f"Цена на билета: {self.ticket_price}, Свободни билети: {self.tickets_available}.")

def search_by_movie_id(movie_list, movie_id):
    for movie in movie_list:
        if movie.movie_id == movie_id:
            print("Намерихме филм с посоченото ИД.")
            print("Пълна информация: ")
            movie.info()
            return
    print("Няма филм в видеотеката е посоченото ИД.")

def search_by_genre(movie_list, genre):
    movies_by_genre = []
    for movie in movie_list:
        if movie.genre == genre:
            movies_by_genre.append(movie)

    average_for_genre = 0
    sum_of_prices = 0
    if len(movies_by_genre) > 0:
      for movie in movies_by_genre:
          sum_of_prices += movie.ticket_price
      average_for_genre = sum_of_prices / len(movies_by_genre)
      print(f"Средната цена за жанра е: {average_for_genre}.")
    else:
        print("Няма филми в видеотеката от този жанр.")

    lower_price = []
    if len(movies_by_genre) > 0:
        for movie in movies_by_genre:
            if movie.ticket_price <= average_for_genre:
                lower_price.append(movie)

    if len(lower_price) > 0:
        print("Филми от посочения жанр с цена ≤ средната за жанра: ")
        for movie in lower_price:
            movie.info()
    else:
        print("Няма филми от посочения жанр с цена ≤ средната за жанра.")

def sort_by_tickets_available(movie_list):
    movie_list.sort(key=lambda m: m.tickets_available)
    print("Сортирахте списъка във възходящ ред!")

def delete_by_title(movie_list, title):
    for movie in movie_list.copy():
        if movie.title == title:
            if movie.tickets_available <= 5:
                print(f"Изтрихте билетите на филма '{title}'.")
                movie_list.remove(movie)

def main():
    movie_list = []
    n = int(input("Въведете колко броя филми ще добавите във видеотеката: "))
    for i in range(n):
        movie_id = input("Въведете ID на филма: ")
        title = input("Въведете името на филма: ")
        genre = input("Въведете жанра на филма: ")
        ticket_price = float(input("Въведете цената на билета: "))
        tickets_available = int(input("Въведете броя на свободните билети за този филм: "))
        movie = Movie(movie_id, title, genre, ticket_price, tickets_available)
        movie_list.append(movie)
        print("Успешно добавихте филма към видеотеката!")

    found = False
    title = input("Въведете името на филма, за чиито искате да продадете билети: ")
    for movie in movie_list:
        if movie.title == title:
            count = int(input("Въведете броя на билетите, които искате да продадете: "))
            movie.sell_tickets(count)
            found = True
            break
    if not found:
       print("Не намерихме филм с такова име във видеотеката!")

    found = False
    title = input("Въведете името на филма, което искате да проверите за отстъпка: ")
    for movie in movie_list:
        if movie.title == title:
            movie.discount()
            found = True
            break
    if not found:
        print("Няма филм с такова име във видеотеката!")

    movie_id = input("Въведете ИД-то на филма, който търсите: ")
    search_by_movie_id(movie_list, movie_id)

    genre = input("Въведете жанра на филма, който търсите: ")
    search_by_genre(movie_list, genre)

    sort_by_tickets_available(movie_list)

    title = input("Въвдете името на филма, който искате да изтриете: ")
    delete_by_title(movie_list, title)

main()