import random
import sys

while True:
    try:
        m = int(input("Въведете цяло число в интервала (30 ≤ m ≤ 80): "))
        if 30 <= m <= 80:
            break
        else:
            print("Моля въведете число в посочения интервал!")
    except ValueError:
        print("Моля въведете валидни данни!")

arr = []
for i in range(m):
    number = random.randint(-9000, 9000)
    arr.append(number)
    print(f"Добавихте числото {number} в списъка!")

count_negative_even_last_digit = 0
for number in arr:
    if number < 0:
        last_digit = abs(number) % 10
        if last_digit % 2 == 0:
            count_negative_even_last_digit += 1
if count_negative_even_last_digit != 0:
    print(f"Броя на числата, които са отрицателни и имат четна последна цифра е: {count_negative_even_last_digit}.")
else:
    print("Няма отрицателни числа с четна последна цифра в листа!")

min_number = sys.maxsize
for number in arr:
    if 10 <= number <= 99:
        if number < min_number:
            min_number = number
if min_number != sys.maxsize:
   print(f"Най-малкото двуцифрено положително число е: {min_number}.")
else:
    print("Няма двуцифрени положителни числа!")

arr_2 = []
for number in arr:
    if number % 3 == 0:
        str_number = str(number)
        for digit in str_number:
            if digit == "3":
                arr_2.append(number)
                print(f"Добавихте числото {number} във втория списък!")
                break

count_elements_at_even_idx = 0
for idx in range(len(arr_2)):
    if idx % 2 == 0:
        count_elements_at_even_idx += 1
if count_elements_at_even_idx != 0:
    print(f"Броя на елементите на четни индекси е: {count_elements_at_even_idx}.")
else:
    print("Няма елементи на четни индекси в листа!")

for idx in range(len(arr_2)):
    if arr_2[idx] < 0:
        print(f"Заменихте числото {arr_2[idx]} с -33.")
        arr_2[idx] = -33

if len(arr_2) == 0:
    print("Вторият лист arr_2 е празен!")