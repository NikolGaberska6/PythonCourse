class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Вие взехте {self.title}!")
        else:
            print(f"Книгата {self.title} вече е взета!")

    def return_book(self):
        if not self.is_available: 
            self.is_available = True
            print(f"Върнахте книгата {self.title}!")
        else:
            print("Книгата вече е върната!")

    def info(self):
        if self.is_available:
         status = "налична"
        else:
            status = "заета"
        print(f"Заглавие | {self.title} Автор | {self.author} Статус | {status}")

library = []
while True:
    print("---------------------------")
    print("           МЕНЮ            ")
    print("---------------------------")

    print("1.Добавяне на книга")
    print("2.Заемане на книга")
    print("3.Връщане на книга")
    print("4.Списък на всички книги")
    print("0.Изход")
    choice = int(input("Изберете опция: "))

    if choice == 1:
        title = input("Въведете заглавието на книгата: ")
        author = input("Въведете автора на книгата: ")
        book = Book(title, author)
        library.append(book)

    elif choice == 2:
        title = input("Въведете заглавието на книгата, която искате да заемете: ")
        for b in library:
            if b.title.lower() == title.lower():
                b.borrow()
                break
            else:
                print("Няма такава книга в библиотеката!")
                break

    elif choice == 3:
        title = input("Въведете заглавието на книгата, която искате да върнете: ")
        for b in library:
            if b.title == title:
                b.return_book()
                break
            else:
                print("Книгата е в библиотеката!")
                break

    elif choice == 4:
        for b in library:
            b.info()