class StudentCourse:
    def __init__(self, course_id, course_name, lecturer, fee, student_count):
        self.course_id = course_id
        self.course_name = course_name
        self.lecturer = lecturer
        self.fee = fee
        self.student_count = student_count

    def enroll(self, count):
        print(f"Записват се още {count} ученици.")
        self.student_count += count
        print(f"Новата бройка на ученици е: {self.student_count}.")

    def discount(self):
        if self.fee > 1000:
            discount = 0.1 * self.fee
            print("Отстъпката е равна на 10% от таксата.")
            self.fee -= discount
            print(f"Новата цена на таксата е: {self.fee} лв.")
        elif 500 <= self.fee <= 1000:
            discount = 0.05 * self.fee
            print("Отстъпката е равна на 5% от таксата.")
            self.fee -= discount
            print(f"Новата цена на таксата е: {self.fee} лв.")
        else:
            print("Няма отстъпка!")
            print(f"Цената на таксата е: {self.fee} лв.")


    def info(self):
        print(f"ID а курса: {self.course_id}, Името на курса: { self.course_name}, "
              f"Преподавател: {self.lecturer}, Такса: {self.fee}, Брой на учениците в курса: {self.student_count}.")

def search_by_id(course_list, course_id):
    for course in course_list:
        if course.course_id == course_id:
            print("Намерихте курс с даденото ID.")
            return
    print("Няма курс с такова ID.")

def search_by_lecturer(course_list, lecturer):
    lecturer_list = []
    for course in course_list:
        if course.lecturer.lower() == lecturer.lower():
            lecturer_list.append(course)

    average = 0
    sum_of_fee = 0
    if len(lecturer_list) > 0:
      for course in lecturer_list: #за всеки курс на дадения преподавател
          sum_of_fee += course.fee
    else:
        print("В списъка с курсове няма курс на дадения преподавател!")

    if len(lecturer_list) > 0:
        average = sum_of_fee / len(lecturer_list)
        print(f"Средна такса за преподавателя е: {average}")

    result = []
    for course in lecturer_list:
        if course.fee <= average:
            result.append(course)

    if len(result) > 0:
        print("Курсовете на дадения преодавател с такса ≤ средната за преподавателя са: ")
        for course in result:
            course.info()
    else:
        print("Няма курсове на дадения преподавател с такса ≤ средната за преподавателя.")


def sort_by_student(course_list):
    course_list.sort(key=lambda c: c.student_count)
    print("Сортирахте списъка във възхидящ ред!")

def delete_by_name(course_list, course_name):
    for course in course_list:
        if course.course_name.lower() == course_name.lower():
            if course.student_count <= 10:
              print(f"Успешно изтрихте курса с име {course_name} от списъка с курсове!")
              course_list.remove(course)

def main():
    course_list = []
    num = int(input("Въведете броя на курсовете, които искате да добавите: "))
    for i in range(num):
        course_id = input("Въведете ID-то на курса, който искате да добавите: ")
        course_name = input("Въведете името на курса: ")
        lecturer = input("Въведете името на преподавателя: ")
        fee = float(input("Въведете сумата на таксата: "))
        student_count = int(input("Въведете броя на учениците, записани в курса: "))
        course = StudentCourse(course_id, course_name, lecturer, fee, student_count)
        course_list.append(course)
        print("Успешно добавихте курса към списъка с курсове!")

    course_id = input("Въведете ID-то на курса, към който искате да добавите още ученици: ")
    for course in course_list:
        if course.course_id == course_id:
            count = int(input("Въведете броя на учениците, които искате да добавите: "))
            course.enroll(count)

    course_id = input("Въведете ID-то на курса, който търсите: ")
    search_by_id(course_list, course_id)

    lecturer = input("Въведете името на преподавателя, по който търсите: ")
    search_by_lecturer(course_list, lecturer)

    sort_by_student(course_list)

    course_name = input("Въведете името на курса, който искате да изтриете: ")
    delete_by_name(course_list, course_name)

main()
