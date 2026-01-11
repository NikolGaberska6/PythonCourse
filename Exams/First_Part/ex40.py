import random
import sys

while True:
    m = int(input("Въведете число в интервала (25 < m < 70): "))
    if 25 < m < 70:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_L = []
p = random.randint(-10000, -3000)
q = random.randint(5000, 12000)
for i in range(m):
    number = random.randint(p, q)
    list_L.append(number)
    print(f"Успешно добавихте числото {number} в списъка с числа!")

count_numbers_with_more_even_digits = 0
for number in list_L:
    count_even_digits = 0
    count_odd_digits = 0
    str_number = str(abs(number))
    for digit in str_number:
        if int(digit) % 2 == 0:
            count_even_digits += 1
        else:
            count_odd_digits += 1
    if count_even_digits > count_odd_digits:
        count_numbers_with_more_even_digits += 1
if count_numbers_with_more_even_digits != 0:
    print(f"Броя на числата, които имат повече четни цифри от нечетни: {count_numbers_with_more_even_digits}")
else:
    print("Няма числа в листа, които имат повече четни от нечетни цифри!")

max_number = -sys.maxsize
for number in list_L:
    if number < 0:
      if number > max_number:
          max_number = number
if max_number != -sys.maxsize:
    print(f"Най-голямото отрицателно число е: {max_number}")
else:
    print("В листа няма отрицателни числа!")

list_L2 = []
for number in list_L:
    sum_of_digits = 0
    str_number = str(abs(number))
    for digit in str_number:
        sum_of_digits += int(digit)
    if sum_of_digits % 3 == 0:
        list_L2.append(number)
        print(f"Додавихте числото {number} в новия списък!")

count_nums_idx_del4 = 0
for idx in range(len(list_L2)):
    if idx % 4 == 0:
        count_nums_idx_del4 += 1
if count_nums_idx_del4 != 0:
    print(f"Броя на елементите в L2, които се намират на индекси, кратни на 4 е: {count_nums_idx_del4}")
else:
    print("Няма елементи в L2 на индекси, кратни на 4!")

for idx in range(len(list_L2)):
    current_num = list_L2[idx]
    str_current_num = str(abs(current_num))
    for digit in str_current_num:
        if int(digit) == 0:
            list_L2[idx] = 0
            print(f"Заменихте числото {current_num} с 0.")
            break

if len(list_L2) > len(list_L):
    list_L2 = list_L2[2:]
    print("Изтрихте първите 2 елемента от list_L2!")