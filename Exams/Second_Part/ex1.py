class Library:
    def __init__(self, isbn, title, author, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def borrow(self, n):
        if self.copies >= n:
            self.copies = self.copies - n
            print(f"Взехте {n} на брой копя от библиотеката.")
            print(f"Останала наличност: {self.copies}")
        else:
            print("Няма достатъчна наличност!")

    def apply_discount(self):
        if 20 < self.price < 50:
            discount = 0.1 * self.price
            print(f"Отстъпката ви е: {discount}")
            self.price = self.price - discount
            print(f"Новата цена с отстъпката е: {self.price} лв.")
        elif 10 < self.price < 20:
            discount = 0.05 * self.price
            print(f"Отстъпката ви е: {discount}")
            self.price = self.price - discount
            print(f"Новата цена с отстъпката е: {self.price} лв.")
        else:
            print("Няма остъпка!")
            print(f"Цената е: {self.price}")

    def info(self):
        print(f"Баркод: {self.isbn}, Заглавие: {self.title}, Автор: {self.author},"
              f" Цена: {self.price}, Копия: {self.copies}")

book_list = []
n = int(input("Въведете броя на книгите, които искате да добавите: "))
for i in range(n):
    isbn = input("Въведете баркода на книгата: ")
    title = input("Въведете заглавието на книгата: ")
    author = input("Въведете името на автора на книгата: ")
    price = float(input("Въведете цената на книгата: "))
    copies = int(input("Въвдете броя на копията на книгата: "))
    book = Library(isbn, title, author, price, copies)
    book_list.append(book)

def search_by_isbn(isbn):
    found = False
    for book in book_list:
        if book.isbn == isbn:
            book.info()
            found = True
            break
    if not found:
        print("Книга с такъв ISBN не е намерена!")

def search_by_author(author):
    author_books = []
    for book in book_list:
        if book.author == author:
            author_books.append(book)
    if len(author_books) == 0:
        print(f"Няма книги на {author}")

    total_price = 0
    for book in author_books:
        total_price += book.price
    avg_price = total_price/len(author_books)
    print(f"Средната цена на книгите на {author} e {avg_price:.2f} лв")

    result = []
    for book in author_books:
        if book.price <= avg_price:
            result.append(book)

    if len(result) > 0:
        print("Книги с цена <= средната цена:")
        for book in result:
            print(book.info())
    else:
        print("Няма книги с цена по-ниска или равна на средната.")

def delete_by_title(title):
    for book in book_list.copy():
        if book.title == title:
            if book.copies <= 2:
                book_list.remove(book)

# -----------------------------
# Тук започва изпълнението без меню
# -----------------------------

# 1️⃣ Търсене на книга по ISBN
isbn = input("Въвдете баркода, по който търсите: ")
search_by_isbn(isbn)

# 2️⃣ Търсене на книги по автор
author_search = input("Въведете автора за търсене: ")
search_by_author(author_search)

# 4️⃣ Изтриване на книги с ≤2 копия по заглавие
title = input("Въведете заглавието на книгата, която искате да изтриете: ")
delete_by_title(title)