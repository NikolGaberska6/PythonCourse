class Student:
    def __init__(self, name, faculty_number, grade, specialty):
        self.name = name
        self.faculty_number = faculty_number
        self.grade = grade
        self.specialty = specialty

    def student_info(self):
        print("----Цялата информация за студента----")
        print(f"Име: {self.name}, Факултетен номер: {self.faculty_number}, "
              f"Оценка: {self.grade}, Специалност: {self.specialty}.")

    def change_grade(self):
        print("----Промяна на оценката на студента!----")
        new_grade = float(input("Въведете новата оценка на студента: "))
        self.grade = new_grade
        print("Оценката бе променена успешно!")

def input_student():
    print("----Добавяне на студент----")
    name = input("Въведете името на студента: ")
    faculty_number = input("Въведете факултетния номе рна студента: ")
    grade = float(input("Въведете оценката на студента: "))
    specialty = input("Въведете специалността на студента: ")
    return Student(name, faculty_number, grade, specialty)

def search_by_specialty(student_list, specialty):
    students_of_specialty = []
    for student in student_list:
        if student.specialty == specialty:
            students_of_specialty.append(student)
    if len(students_of_specialty) > 0:
        print("Всички студенти от посочената специалност са: ")
        for student in students_of_specialty:
            student.student_info()
    else:
        print("Students not found")

def add_student(student_list, new_student):
    student_list.append(new_student)
    print("Успешно добавихте новия студент към списъка!")

def main():
    student_list = []
    n = int(input("Въведете броя на студентите, които искате да добавите: "))
    for i in range(n):
        student = input_student()
        student_list.append(student)
        print("Успешно добавихте студента към списъка!")

    found = False
    faculty_number = input("Въведете факултетния номер на студента, "
                           "чиято оценка искате да промените: ")
    for student in student_list:
        if student.faculty_number == faculty_number:
            found = True
            print("Студентът е намерен!")
            student.change_grade()
    if not found:
        print("Не е намерен студент с посочения факултетен номер!")

    specialty = input("Въведете специалността, по която търсите: ")
    search_by_specialty(student_list, specialty)

    new_student = input_student()
    add_student(student_list, new_student)

main()