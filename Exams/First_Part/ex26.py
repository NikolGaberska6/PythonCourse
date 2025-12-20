grades = []
for i in range(25):
    number = int(input("Въведете число, което искате да добавите в листа: "))
    grades.append(number)

count_excellent = 0
for grade in grades:
    if grade >= 90:
        count_excellent += 1
if count_excellent != 0:
    print(f"Броя на отличните оценки е: {count_excellent}.")
else:
    print("Няма отлични оценки!")

failures = []
for grade in grades:
    if grade < 50:
      failures.append(grade)
      print("Добавихте слаба оценка към втория лист!")

if len(failures) > 0:
  sum_of_failures = sum(failures)
  average = sum_of_failures/len(failures)
  print(f"Средната стойност на списъка със слабите оценки е: {average}.")

max_grade = max(grades)
min_grade = min(grades)
sum_of_min_max = max_grade + min_grade
print(f"Сумата на най-високата и най-ниската оценка в grades е: {sum_of_min_max}.")
failures.append(sum_of_min_max)
