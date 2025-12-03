class Student:
    def __init__(self, name, faculty_number):
        self.name = name
        self.faculty_number = faculty_number
        self.grades = []

    def add_grade(self, grade):
        if 2 <= grade <= 6:
            self.grades.append(grade)
            print(f"Добавена оценка {grade} за студент {self.name}.")

    def average_grades(self):
        if len(self.grades) == 0:
            return "Няма въведете оценки в списъка!"
        else:
         return sum(self.grades) / len(self.grades)

    def info(self):
        avg = self.average_grades()
        print(f"Ученик | {self.name}, "
              f"Факултетен номер {self.faculty_number}, "
              f"Среден успех {avg}.2f")

#Главната част на програмата
students = []
def find_by_fac_number():
    f_number = input("Въведете факултетен номер, по който искате да търсите: ")
    for s in students:
        if s.f_number == f_number:
            s.info()


while True:
    print("----------------------------------")
    print("                  МЕНЮ            ")
    print("----------------------------------")
    print("1.Добавяне на нов студент")
    print("2.Добавяне на оценка на студент")
    print("3.Показване информация за студент")
    print("4.Списък на всички студенти")
    print("0.Изход")
    choice = int(input("Въведете своя избор: "))

    if choice == 1:
        name = input("Въведете име на студента: ")
        faculty_number = input("Въведете факултетен номер на студента: ")
        student = Student(name, faculty_number)
        students.append(student)

    elif choice == 2:
        name = input("Въведете на кой студент искате да добавите оценката: ")
        grade = int(input("Въведете оценка на студента: "))
        for s in students:
            if s.name == name:
                s.add_grade(grade)

    elif choice == 3:
        name = input("Въведете име на студент, за койтон искате да покажете информация: ")
        for s in students:
            if s.name == name:
                s.info()

    elif choice == 4:
        for s in students:
            print(s.name)

    elif choice == 0:
        print("Довиждане!")
        break