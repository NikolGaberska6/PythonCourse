import random
import sys

while True:
    m = int(input("Въведете число в интервала (30 < m < 80): "))
    if 30 < m < 80:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_A = []
p = random.randint(-20000, -5000)
q = random.randint(4000, 15000)
for i in range(m):
    number = random.randint(p, q)
    list_A.append(number)
    print(f"Успешно добавихте числото {number} в листа!")

count_more_odd_digits = 0
for number in list_A:
    count_even_digits = 0
    count_odd_digits = 0
    str_number = str(abs(number))
    for digit in str_number:
        if int(digit) % 2 == 0:
            count_even_digits += 1
        else:
            count_odd_digits += 1
    if count_odd_digits > count_even_digits:
        count_more_odd_digits += 1
if count_more_odd_digits != 0:
    print(f"Броя на числата, които съдържат повече нечетни цифри от четни е: {count_more_odd_digits}.")
else:
    print("Няма числа в листа, които да съдържат повече нечетни от четни цифри!")

min_number = sys.maxsize
for number in list_A:
    if number > 0:
        if number < min_number:
            min_number = number
if min_number != sys.maxsize:
    print(f"Най-малкото положително число е: {min_number}")
else:
    print("Няма най-малко положително число в листа!")

list_B = []
for number in list_A:
    multiply_digits = 1
    str_number = str(abs(number))
    for digit in str_number:
        multiply_digits *= int(digit)
    if multiply_digits % 2 == 0:
        list_B.append(number)
        print(f"Успешно добавихте числото {number} във втория лист!")

count_elements_odd_idx = 0
for idx in range(len(list_B)):
    if idx % 2 != 0:
        count_elements_odd_idx += 1
if count_elements_odd_idx != 0:
    print(f"Броя на елементите в B, които се намират на нечетни индекси е: {count_elements_odd_idx}.")
else:
    print("Няма елементи в листа на нечетен индекс!")

for idx in range(len(list_B)):
    if list_B[idx] < 0:
       print(f"Заменихте числото {list_B[idx]} с -1!")
       list_B[idx] = -1

if len(list_B) < len(list_A):
    sum_of_all_elements = 0
    for number in list_A:
        sum_of_all_elements += number
    print(f"Сумата на всички елементи в първия лист е: {sum_of_all_elements}")
    list_B.append(sum_of_all_elements)
    print(f"Добавихте {sum_of_all_elements} в края на втория лист!")