class Course:
    def __init__(self, code, name, lecturer, hours, student_count):
        self.code = code
        self.name = name
        self.lecturer = lecturer
        self.hours = hours
        self.student_count = student_count

    def add_student(self, n):
        print(f"Добавихте {n} на брой студенти в посочения курс!")
        self.student_count += n
        print(f"Новия брой на студентите е: {self.student_count}")

    def is_popular(self):
        if self.student_count > 30:
            print("Курсът е популярен!")

    def info(self):
        print(f"Koд: {self.code}, Име: {self.name}, Преподавател: {self.lecturer}, "
              f"Брой часове: {self.hours}, Брой студенти: {self.student_count}.")

def search_by_lecturer(courses, lecturer):
    courses_from_lecturer = []
    for course in courses:
        if course.lecturer == lecturer:
            courses_from_lecturer.append(course)
    if len(courses_from_lecturer) > 0:
        print("Всички курсове на посочения преподавател: ")
        for course in courses_from_lecturer:
            course.info()
    else:
        print("Няма курсове на посочения преподавател!")

def average_hours(courses):
    sum_of_all_hours = 0
    average_of_all_hours = 0
    for course in courses:
        sum_of_all_hours += course.hours
    if sum_of_all_hours != 0:
        average_of_all_hours = sum_of_all_hours / len(courses)
        print(f"Средния брой часове на всички курсове е: {average_of_all_hours}")
    else:
        print("Списъкът с курсове е празен!")
    return average_of_all_hours

def sort_by_students(courses):
    courses.sort(key=lambda c: c.student_count)
    print("Сортирахте курсовете по брой студенти във възходящ ред!")
    print("Сортирания списък: ")
    for course in courses:
        course.info()

def delete_small_courses(courses):
    deleted_courses = 0
    for course in courses.copy():
        if course.student_count < 5:
            deleted_courses += 1
            print(f"Изтрихте курса с код {course.code} от списъка с курсове!")
            courses.remove(course)
    if deleted_courses != 0:
        print(f"Броя на изтритите курсове е: {deleted_courses}")
    else:
        print("Няма курсове с по-малко от 5 студенти в списъка с курсове!")

def main():
    courses = []
    n = int(input("Въведете броя на курсовете, които искате да добавите: "))
    for i in range(n):
        code = input("Въведете кода на курса, които искате да добавите: ")
        name = input("Въведете името на курса, които искате да добавите: ")
        lecturer = input("Въведете преподавателя на курса, които искате да добавите: ")
        hours = int(input("Въведете брой часове на курса, които искате да добавите: "))
        student_count = int(input("Въведете броя на студентите на курса, които искате да добавите: "))
        course = Course(code, name, lecturer, hours, student_count)
        courses.append(course)
        print("Успешно добавихте курса към списъка с курсове!")

    found = False
    code = input("Въведете кода на курса, към който искате да добавите студенти: ")
    for course in courses:
        if course.code == code:
            found = True
            n = int(input("Въведете броя на студентите, които искате да добавите: "))
            course.add_student(n)
    if not found:
        print("Няма намерен курс с посочения код в списъка!")

    found = False
    code = input("Въведете кода на курса, който искате да проверите за популярност: ")
    for course in courses:
        if course.code == code:
            found = True
            course.is_popular()
    if not found:
        print("Няма намерен курс с посочения код в списъка!")

    lecturer = input("Въведете преподавателя на курса, по който търсите: ")
    search_by_lecturer(courses, lecturer)

    average_hours(courses)
    sort_by_students(courses)
    delete_small_courses(courses)

main()
