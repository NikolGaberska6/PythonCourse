class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def book_info(self):
        print("---Цялата информация за книгата---")
        print(f"Заглавие: {self.title}, Автор: {self.author}, "
              f"Година на издаване: {self.year}, Цена: {self.price}.")

    def change_price(self):
        print("---Промяна на цената на книгата---")
        new_price = float(input("Въведете новата цена на книгата: "))
        self.price = new_price
        print("Цената на книгата бе променена успешно!")

def input_book():
    print("---Добавяне на книга---")
    title = input("Въведете заглавието на книгата, която искате да добавите: ")
    author = input("Въведете автора на книгата, която искате да добавите: ")
    year = int(input("Въведете годината на издаване на книгата, която искате да добавите: "))
    price = float(input("Въведете цената на книгата, която искате да добавите: "))
    return Book(title, author, year, price)

def search_by_author(book_list, author):
    book_from_author = []
    for book in book_list:
        if book.author.lower() == author.lower():
            book_from_author.append(book)
    if len(book_from_author) > 0:
        print("Всички книги на посочения автор са: ")
        for book in book_from_author:
            book.book_info()
    else:
        print("No books found")

def add_book(book_list, new_book):
    book_list.append(new_book)
    print("Успешно добавихте книгата в списъка!")

def main():
    book_list = []
    n = int(input("Въведете броя на книгите, които искате да добавите: "))
    for i in range(n):
        book = input_book()
        book_list.append(book)
        print("Книгата бе успешно добавена в списъка!")

    found = False
    title = input("Въведете заглавието на книгата, на която искате "
                  "да промените цената: ")
    for book in book_list:
        if book.title.lower() == title.lower():
            found = True
            print("Книгата е намерена!")
            book.change_price()
    if not found:
        print("Не е намерена книга с посоченото заглавие!")

    author = input("Въведете автора на книгата, по който търсите: ")
    search_by_author(book_list, author)

    new_book = input_book()
    add_book(book_list, new_book)

main()