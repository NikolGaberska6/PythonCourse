class Students:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 2 <= grade <= 6:
            self.grades.append(grade)
            print(f"Оценката '{grade}' е добавена в библиотеката.") #ако е с print резултата само се принтира на конзолара, но не може да се преизползва
        else:
            print("Грешка!")

    def average(self):
        if len(self.grades) != 0:
          return sum(self.grades)/len(self.grades) #ако е с return резултата може да се преизползва
        else:
            return "Списъкът е празен!"

    def status(self):
        avg = self.average()
        if avg >= 5.5:
            return "Отличен"
        elif avg >= 4.5:
            return "Много добър"
        elif avg >= 3.5:
            return "Добър"
        elif avg >= 3:
            return "Среден"
        else:
            return "Слаб"

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        total = 0
        if len(self.students) != 0:
            for student in self.students:
                total += student.average()
        return total/len(self.students)

    def top_student(self):
        best_student = self.students[0]
        for student in self.students:
            if student.average() > best_student.average():
                best_student = student
        return best_student


classroom = Classroom()
#ако имената и оценките са въведени от конзолата
s1 = Students("Ivan")
s1.grades = [4, 5, 6]

s2 = Students("Maria")
s2.grades = [5, 6, 5.5]

s3 = Students("Georgi")
s3.grades = [3, 4, 4.5]

# Добавяме учениците в класа
classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(s3)

#ако имената и оценките са въведени от потребителя
# while True:
#     name = input("Въведи име на ученика (или 'stop' за край): ")
#     if name.lower() == "stop":
#         break
#     else:
#         student = Students(name)
#
#     while True:
#         grade_input = input("Въведете оценка на ученика (или 'done' за край): ")
#         if grade_input.lower() == "done":
#             break
#         else:
#             grade_input = int(grade_input)
#             student.add_grade(grade_input)
#
#     classroom.add_student(student)

print("\n============= РЕЗУЛТАТИ =============")
for s in classroom.students:
    print(f"\nУченик: {s.name}")
    print(f"Оценки: {s.grades}")
    avg = s.average()
    print(f"Среден успех: {avg:.2f}")
    print(f"Статус: {s.status()}")

print("\n======================================")
print(f"Среден успех на класа: {classroom.class_average():.2f}")
top = classroom.top_student()
print(f"Най-добър ученик в класа: {top.name}")
