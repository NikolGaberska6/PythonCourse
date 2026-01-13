class Movie:
    def __init__(self, title, director, genre, rating, duration):
        self.title = title
        self.director = director
        self.genre = genre
        self.rating = rating
        self.duration = duration

    def update_rating(self, new_rating):
        print("Променихте оценката на филма с нова!")
        self.rating = new_rating

    def is_recommended(self):
        if self.rating >= 8:
            print("Филмът се счита за препоръчителен!")

    def info(self):
        print(f"Заглавие: {self.title}, Режисьор: {self.director}, Жанр: {self.genre}, "
              f"Оценка: {self.rating}, Продължителност в минути: {self.duration}.")

def search_by_genre(movies, genre):
    films_of_genre = []
    for movie in movies:
        if movie.genre == genre:
            films_of_genre.append(movie)
    if len(films_of_genre) > 0:
        print("Всички филми от жанра са: ")
        for film in films_of_genre:
            print(film.title, end= " ")
    else:
        print("Няма филми от посочения жанр!")

def top_rated_movies(movies):
    average = 0
    sum_of_rating_all_movie = 0
    for movie in movies:
        sum_of_rating_all_movie += movie.rating
    print(f"Общата оценка на всички филми е: {sum_of_rating_all_movie}.")
    average = sum_of_rating_all_movie/len(movies)
    print(f"Средната оценка на всички филми е: {average}.")

    movies_with_greater_rating = []
    for movie in movies:
        if movie.rating > average:
            movies_with_greater_rating.append(movie)

    if len(movies_with_greater_rating) > 0:
        print("Всички филми с оценка по-висока от средната: ")
        for movie in movies_with_greater_rating:
            print(movie.title, end=" ")

    return movies_with_greater_rating

def sort_by_duration(movies):
    movies.sort(key=lambda m: m.duration)
    print("Сортирахте филмите по продължителност във възходящ ред!")
    print("Новия списък с филми е: ")
    for movie in movies:
        print(movie.title, end=" ")

def delete_low_rating(movies):
    is_deleted = False
    for movie in movies.copy():
        if movie.rating < 5:
            is_deleted = True
            print(f"Изтрихте филма: {movie.title}.")
            movies.remove(movie)
    if not is_deleted:
        print("Няма филми с рейтинг по-малък от 5 в списъка с филми!")

def main():
    movies = []
    n = int(input("Въведете броя на филмите, които искате да добавите: "))
    for i in range(n):
        title = input("Въведете заглавието на филма, който искате да добавите: ")
        director = input("Въведете режисьора на филма, който искате да добавите: ")
        genre = input("Въведете жанра на филма, който искате да добавите: ")
        rating = int(input("Въведете оценката на филма, който искате да добавите: "))
        duration = int(input("Въведете профължителността в минути на филма, който искате да добавите: "))
        film = Movie(title, director, genre, rating, duration)
        movies.append(film)

    found = False
    title = input("Въведете заглавието на филма, чиито рейтинг искате да промените: ")
    for film in movies:
        if film.title == title:
            found = True
            new_rating = int(input("Въведете новата оценка на филма: "))
            film.update_rating(new_rating)
    if not found:
        print("Няма филм с посоченото заглавие в списъка с филми!")

    found = False
    title = input("Въведете заглавието на филма, който искате да проверите за препоръчителност: ")
    for film in movies:
        if film.title == title:
            found = True
            film.is_recommended()
    if not found:
        print("Няма филм с посоченото заглавие в списъка с филми!")

    genre = input("Въведете жанра на филма, по който търсите: ")
    search_by_genre(movies, genre)

    top_rated_movies(movies)

    sort_by_duration(movies)

    delete_low_rating(movies)

main()