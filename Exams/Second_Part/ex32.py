class Cinema:
    def __init__(self, movie_title, genre, price_of_ticket,
                 start_time, duration, movie_hall):
        self.movie_title = movie_title
        self.genre = genre
        self.price_of_ticket = price_of_ticket
        self.start_time = start_time
        self.duration = duration
        self.movie_hall = movie_hall

    def movie_info(self):
        print("Информация за прожекцията: ")
        print(f"Заглавие: {self.movie_title}, Жанр: {self.genre}, "
              f"Цена на билета: {self.price_of_ticket}, Начало на прожекцията: {self.start_time}, "
              f"Продължителност: {self.duration}, Номер на залата: {self.movie_hall}.")

    def change_hall(self):
        new_hall = int(input("Въведете нов номер на зала: "))
        self.movie_hall = new_hall
        print("Номера на залата е променен успешно!")


def input_movie():
    print("Моля въведете данните на прожекцията, която искате да добавите!")
    movie_title = input("Заглавие на филма: ")
    genre = input("Жанр: ")
    price = float(input("Цена на билет: "))
    start_time = input("Начален час: ")
    duration = int(input("Продължителност (минути): "))
    hall = int(input("Номер на зала: "))
    return Cinema(movie_title, genre, price, start_time, duration, hall)

def search_by_time(movie_list, time):
    found = False
    for movie in movie_list:
        if movie.start_time == time:
            found = True
            movie.info()
    if not found:
        print("Movies not found!")

def add_movie(movie_list, new_movie):
    movie_list.append(new_movie)
    print("Прожекцията е успешно добавена в списъка!")

def main():
    movie_list = []
    n = int(input("Въведете броя на прожекциите, които искате да добавите: "))
    for i in range(n):
        movie = input_movie()
        movie_list.append(movie)
        print(f"Успешно добавихте прожекция с име: {movie.movie_title}!")

    found = False
    movie_hall = int(input("Въведете номера на залата, който искате да промените: "))
    for movie in movie_list:
        if movie.movie_hall == movie_hall:
            found = True
            movie.change_hall()
    if not found:
        print("Не е намерена зала с посочения номер!")

    time = input("Въвдете началния час, по който търсите: ")
    search_by_time(movie_list,  time)

    print("Добавяне на прожекция!")
    new_movie = input_movie()
    add_movie(movie_list, new_movie)

main()
