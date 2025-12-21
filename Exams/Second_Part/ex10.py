class Library:
    def __init__(self, isbn, title, author, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def borrow(self, count):
        count = int(input("Въведете колко копия искате да вземете: "))
        if self.copies >= count:
            print(f"Заехте {count} копия.")
            self.copies = self.copies - count
            print(f"Остават: {self.copies}")

    def discount(self):
        if 20 <= self.price <= 40:
            discount = self.price * 0.1
            print("Отстъпката е 10% от цената.")
            self.price = self.price - discount
            print(f"Новата цена е: {self.price}")
        elif 10 <= self.price < 20:
            discount = self.price * 0.15
            print("Отстъпката е 15% от цената.")
            self.price = self.price - discount
            print(f"Новата цена е: {self.price}")
        else:
            print("Нямате отстъпка!")

    def info(self):
        print("Информация за книгата: ")
        print(f"ISBN номер: {self.isbn}, Заглавие: {self.title}, Автор: {self.author}, "
              f"Цена: {self.price}, Бройки: {self.copies}.")

book_list = []
n = int(input("Въведете броя на книгите, които искате да добавите: "))
for i in range(n):
    isbn = input("ISBN номер на книгата: ")
    title = input("Заглавие на книгата: ")
    author = input("Автор на книгата: ")
    price = float(input("Цената на книгата: "))
    copies = int(input("Бройки от книгата: "))
    book = Library(isbn, title, author, price, copies)
    book_list.append(book)
    print("Успешно добавихте книгата в листа!")

def search_by_isbn(book_list, isbn):
    for book in book_list:
        if book.isbn == isbn:
            book.info()
            return
    print("Грешка! Не е намерена книга с такъв ISBN номер!")

def search_by_author(book_list, author):
    books_by_author = []
    average_price = 0

    for book in book_list:
        if book.author == author:
            books_by_author.append(book) #всички книги на автора в лист

    price_for_all_books_by_author = 0 #общата цена на книгите в листа
    for book in books_by_author:
        price_for_all_books_by_author += book.price
    if len(books_by_author) > 0:
       average_price = price_for_all_books_by_author / len(books_by_author)# средната цена на книгите в листа
    else:
        print("Няма книги на този автор в листа!")

    result = []
    for book in books_by_author:
        if book.price <= average_price:
            result.append(book)

    if len(result) > 0:
       print(f"Книги на автора {author} с цена ≤ средната за автора {average_price}:  ")
       for book in result:
          book.info()
    else:
        print("Няма книги на автора с цена ≤ средната за автора!")

def sort_by_copies(book_list):
    book_list.sort(key=lambda b: b.copies)
    print("Сортирахте по брой копия във възходящ ред!")

def delete_by_title(book_list, title):
    for book in book_list.copy():
        if book.title == title and book.copies <= 2:
            print(f"Успешно изтрихте книгата {book.title} от листа!")
            book_list.remove(book)


isbn = input("Въведете ISBN номер, по който търсите: ")
search_by_isbn(book_list, isbn)

author = input("Въведете автора, по който търсите: ")
search_by_author(book_list, author)

sort_by_copies(book_list)

title = input("Въведете заглавието на книгата, която искате да изтриете: ")
delete_by_title(book_list, title)
