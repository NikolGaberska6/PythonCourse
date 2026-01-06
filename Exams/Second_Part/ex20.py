class Student:
    def __init__(self, fn, name, specialty, grade, credits):
        self.fn = fn
        self.name = name
        self.specialty = specialty
        self.grade = grade
        self.credits = credits

    def add_credits(self, n):
        print(f"Добавихте {n} брой кредити на студента!")
        self.credits += n
        print(f"Новия брой кредити е: {self.credits}")

    def scholarship(self):
        if self.grade >= 5.50:
            scholarship = 100
            print("На ученикът му се отпуска се стипендия в размер на 100 лв.")
        elif 5.00 <= self.grade <= 5.49:
            scholarship = 50
            print("На ученикът му се отпуска се стипендия в размер на 50 лв.")
        else:
            print("На ученикът не му се допуска стипендия!")

    def info(self):
        print(f"Факултетенн номер: {self.fn}, Име: {self.name}, "
              f"Специалност: {self.specialty}, Успех: {self.grade}, "
              f"Кредити: {self.credits}.")

def search_by_fn(students, fn):
    for student in students:
        if student.fn == fn:
            print("Намерихме ученик в списъка с посочения факултетен номер!")
            print("Пълна информация за ученика: ")
            student.info()
            return
    print("Няма намерен ученик в списъка с посочения факултетен номер!")

def students_above_average(students):
    average_grade_of_all_students = 0
    sum_of_grades_of_students = 0
    for student in students:
        sum_of_grades_of_students += student.grade

    average_grade_of_all_students = sum_of_grades_of_students/len(students)
    print(f"Средния успех на всички студенти е: {average_grade_of_all_students:.2f}.")

    students_with_greater_grade = []
    for student in students:
        if student.grade >= average_grade_of_all_students:
            students_with_greater_grade.append(student)

    if len(students_with_greater_grade) > 0:
        print("Всички студентите, чийто успех е по-голям или равен на средния са: ")
        for student in students_with_greater_grade:
            student.info()
    else:
        print("Няма студенти в списъка, чийто успех е по-голям или равен на средния.")

    return students_with_greater_grade

def sort_by_credits(students):
    students.sort(key=lambda s: s.credits)
    print("Сортирахте студентите по брой кредити във възходящ ред!")
    print("Сортирания списък: ")
    for student in students:
        student.info()

def delete_low_grade(students):
    for student in students.copy():
        if student.grade < 3.00:
            print(f"Изтрихте студента {student.name} от списъка!")
            students.remove(student)

def main():
    students = []
    numbers_of_students = int(input("Въведете броя на студентите, които искате да добавите: "))
    for i in range(numbers_of_students):
        fn = input("Въведете факултетния номер на студента, който искате да добавите: ")
        name = input("Въведете името на студента, който искате да добавите: ")
        specialty = input("Въведете специалността на студента, който искате да добавите: ")
        grade = float(input("Въведете оценката на студента, който искате да добавите: "))
        credits = int(input("Въведете кредитите на студента, който искате да добавите: "))
        student = Student(fn, name, specialty, grade, credits)
        students.append(student)
        print("Успешно добавихте студента в списъка със студенти!")

    is_found = False
    fn = input("Въведете факултетния номер на студента, на който искате да добавите кредити: ")
    for student in students:
        if student.fn == fn:
            is_found = True
            n = int(input("Въведете броя на кредитите, които искате да добавите: "))
            student.add_credits(n)
    if not is_found:
        print("Не е намерен студент с посочения факултетен номер!")

    is_found = False
    fn = input("Въведете факултетния номер на студента, на който искате да проверите за стипендия: ")
    for student in students:
        if student.fn == fn:
            is_found = True
            student.scholarship()
    if not is_found:
        print("Не е намерен студент с посочения факултетен номер!")

    fn = input("Въведете факултетния номер на студента, по който търсите: ")
    search_by_fn(students, fn)

    students_above_average(students)

    sort_by_credits(students)

    delete_low_grade(students)

main()