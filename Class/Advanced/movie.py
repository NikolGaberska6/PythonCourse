class Movie:
    def __init__(self, title, director, year, rating, genre):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        self.genre = genre

    def info(self):
        return (f"Заглавие: {self.title}\n "
                f"Режисьор: {self.director}\n "
                f"Година: {self.year}\n"
                f"Рейтинг: {self.rating}\n"
                
                f"Жанр: {self.genre}")

    def update_rating(self, new_rating):
        if 1 <= new_rating <= 10:
            self.rating = new_rating
            print(f"Рейтингът на {self.title} e обновен на {self.rating}")
        else:
            print("Грешка")

class MovieLibrary:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        print(f"Филмът '{movie.title}' е добавен в библиотеката.")

    def search_by_title(self,title):
        for movie in self.movies:
            if title.lower() == movie.title.lower():
                print(movie.info())
                return
            print("Филмът не е намерен!")
            print("Налични заглавия:")
            for movie in self.movies:
                print("-", movie.title)

    def search_by_genre(self, genre):
        for movie in self.movies:
            if genre.lower() == movie.genre.lower():
                print(f"Филми от жанра: {genre}\n")
                for movie in self.movies:
                    print("-", movie.genre)
                    return
            print(f"Няма филми от жанра '{genre}'")

    def movies_by_director(self,director):
        for movie in self.movies:
            if director.lower() == movie.director:
                print(f"Филми на режисьора '{director}':\n")
                for movie in self.movies:
                    print("-", movie.director)
                    return
            print(f"Няма филми на режисьора '{director}'.")

    def top_rated(self,min_rating):
        for movie in self.movies:
            if movie.rating >= min_rating:
                print("Филми с рейтинг >= на дадения са:\n ")
                for movie in self.movies:
                    print("-", movie.rating)
                    return
            print(f"Няма филми с рейтинг >= {min_rating}.")

movie_library = MovieLibrary()

def menu():
    print("\n=== Меню ===")
    print("1. Добавяне на филм")
    print("2. Търсене по заглавие")
    print("3. Търсене по жанр")
    print("4. Търсене по режисьор")
    print("5. Филми с висок рейтинг")
    print("6. Всички филми")
    print("7. Изход")

while True:
    menu()
    choice = input("Изберете опция: ")

    if choice == "1":
        title = input("Въведи заглавие: ")
        director = input("Въведи режисьор: ")
        year = input("Въведи година на излизане: ")
        rating_input = input("Въведи рейтинг (1-10): ")
        genre = input("Въведи жанр: ")

        movie = Movie(title, director, year, rating_input, genre)
        movie_library.add_movie(movie)

    elif choice == "2":
        title = input("Въведи заглавие за търсене: ")
        movie_library.search_by_title(title)

    elif choice == "3":
        genre = input("Въведи жанр за търсене: ")
        movie_library.search_by_genre(genre)

    elif choice == "4":
        director = input("Въведи режисьор за търсене: ")
        movie_library.movies_by_director(director)

    elif choice == "5":
        min_rating_input = int(input("Минимален рейтинг: "))
        movie_library.top_rated(min_rating_input)

    elif choice == "6":
        for movie in movie_library.movies:
            print("\n" + movie.info())

    elif choice == "7":
        print("Изход от програмата.")
        break

    else:
        print("Невалиден избор, опитай пак.")
