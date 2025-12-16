from math import sqrt
import sys

while True:
    z = int(input("Въведете число в интервала (20 < z < 100): "))
    if 20 < z < 100:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_P = []
while len(list_P) < z:
    number = int(input("Въвдете число в интервала [-9999, 9999]: "))
    if -9999 <= number <= 9999:
        list_P.append(number)
    else:
        print("Моля въведете число в посочения интервал!")

count_numbers_with_even_digits = 0
for number in list_P:
    only_even = True
    current_num = str(abs(number))
    for digit in current_num:
        int_igit = int(digit)
        if int_igit % 2 != 0:
            only_even = False
            break
    if only_even:
        count_numbers_with_even_digits += 1
if count_numbers_with_even_digits != 0:
    print(f"Броя на числата, които съдържат само четни цифри е: {count_numbers_with_even_digits}")

min_number_even_positive = sys.maxsize
for number in list_P:
    if number > 0 and number % 2 == 0:
        if number < min_number_even_positive:
            min_number_even_positive = number
if min_number_even_positive != sys.maxsize:
    print(f"Минималното число, което е положително и четно е {min_number_even_positive}")
else:
    print("Няма положителни и четно минимално число в листа.")

list_Q = []
for number in list_P:
    str_number = str(abs(number))
    for digit in str_number:
        if digit == "9":
            list_Q.append(number)
            print(f"Добавихте {number} към list_Q.")
            break

for idx in range(len(list_Q)):
    if idx % 2 != 0:
        current_num = abs(list_Q[idx])
        square = int(sqrt(current_num))
        print(f"Заменихте числото {current_num} с {square}.")
        list_Q[idx] = square

if len(list_P) > len(list_Q):
    while len(list_Q) < len(list_P):
        list_Q.append(0)
    print("Добавихте нули на по-късия лист, до изравняване.")
elif len(list_Q) > len(list_P):
    while len(list_P) < len(list_Q):
        list_P.append(0)
    print("Добавихте нули на по-късия лист, до изравняване.")


