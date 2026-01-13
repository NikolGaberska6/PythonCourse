import math
import random
import sys

while True:
    m = int(input("Моля въведете число в интервала (50 ≤ m ≤ 120): "))
    if 50 <= m <= 120:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_A = []
for i in range(m):
    number = random.randint(-20000, 20000)
    list_A.append(number)
    print(f"Успешно добавихте числото {number} в листа с числа!")

count_sqr = 0
for number in list_A:
    if number > 0:
        root = math.isqrt(number)
        if root * root == number:
            count_sqr += 1
if count_sqr != 0:
    print(f"Броя на числата, които са съвършени квадрати е: {count_sqr}.")
else:
    print("Няма числа в листа, които да са съвършени квадрати!")

min_element = sys.maxsize
for number in list_A:
    count_digits = 0
    str_number = str(abs(number))
    for digit in str_number:
        count_digits += 1
    if count_digits % 2 != 0:
        if number < min_element:
            min_element = number
if min_element != sys.maxsize:
   print(f"Най-малкия елемент с нечетен брой цифри е: {min_element}.")
else:
    print("Няма най-малък елемент с нечетен брой цифри в листа!")

list_B = []
for number in list_A:
    if number % 5 == 0:
        is_found = False
        str_number = str(abs(number))
        for digit in str_number:
            if digit == "5":
                is_found = True
                break
        if not is_found:
            list_B.append(number)
            print(f"Добавихте числото {number} във втория лист!")

for idx in range(len(list_B)):
    if idx % 4 == 0:
        print(f"Премахнахте числото на {idx} индекс!")
        list_B.remove(list_B[idx])

count_nums = 0
for idx in range(1, len(list_B) - 1):
    if list_B[idx] < 0 :
        if list_B[idx - 1] > 0 and list_B[idx + 1] > 0:
          count_nums += 1
if count_nums != 0:
    print(f"Броя на отрицателните елементи, които се намират между два положителни е: {count_nums}.")
else:
    print("Няма отрицателни елементи, които се намират между два положителни в листа!")

if len(list_A) < len(list_B):
    while len(list_A) != len(list_B):
        list_A.append(0)
    print("Изравнихте дължините на двата списъка!")
elif len(list_B) < len(list_A):
    while len(list_A) != len(list_B):
        list_B.append(0)
    print("Изравнихте дължините на двата списъка!")
else:
    print("Дължините на двата списъка са равни!")

