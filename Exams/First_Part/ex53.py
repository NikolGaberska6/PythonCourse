numbers_list = []
for i in range(15):
    number = float(input("Въведете число, което искате да добавите"
                         "в листа!"))
    numbers_list.append(number)
    print("Числото е успешно добавено!")

max_num = max(numbers_list)
min_num = min(numbers_list)
sum_max_min = max_num + min_num
print("Сумата от максималното и минималното число в "
      f"листа е: {sum_max_min}.")

count_negative = 0
for number in numbers_list:
    if number < 0:
        count_negative += 1
if count_negative != 0:
    print(f"Броя на отрицателните числа в листа е: {count_negative}.")
else:
    print("Няма отрицателни числа в листа!")

positive_list = []
for number in numbers_list:
    if number > 0:
        positive_list.append(number)
        print(f"Успешно добавихте числото {number} във втория лист!")

if len(positive_list) > 0:
    sum_of_el = 0
    average = 0
    for number in positive_list:
        sum_of_el += number
    average = sum_of_el / len(positive_list)
    print("Средноаритметичната стойност на елементите от"
          f"втория списък е: {average:.2f}.")

    min_num2 = min(positive_list)
    max_num2 = max(positive_list)
    diff_max_min = max_num2 - min_num2
    print("Разликата на максималния и минималния елемент в"
          f"листа е: {diff_max_min}")
    positive_list.append(diff_max_min)
    print("Добавихте разликата във втория лист!")

else:
    print("Няма положителни числа в първия листа!")
    print("Вторият лист 'positive_list' е празен!")