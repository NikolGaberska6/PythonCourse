import random
import math

while True:
    n = int(input("Въведете число в интервала (40 ≤ n ≤ 100): "))
    if 40 <= n <= 100:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_A = []
for i in range(n):
    number = random.randint(-15000, 15000)
    list_A.append(number)
    print(f"Успешно добавихте числото {number} в листа с числа!")

pos = []
neg = []

for number in list_A:
    if number < 0:
        neg.append(number)
    elif number > 0:
        pos.append(number)

count_sqr = 0
for number in pos:
    k = math.isqrt(number)
    if k * k == number:
        count_sqr += 1
if count_sqr != 0:
    print(f"Броя на числата, които са квадрати на цели числа е: {count_sqr}")
else:
    print("Няма числа, които са квадрати на цели числа в листа!")

sum_nums_even_count_digits = 0
for number in neg:
    count_digits = 0
    str_number = str(abs(number))
    for digit in str_number:
        count_digits += 1
    if count_digits % 2 == 0:
        sum_nums_even_count_digits += number
if sum_nums_even_count_digits != 0:
    print(f"Сумата на числата, които имат четен брой цифри е: {sum_nums_even_count_digits}")
else:
    print("Няма числа в листа, които имат четен брой цифри!")

list_C = []
for number in list_A:
    if number % 9 == 0 or number % 11 == 0:
        list_C.append(number)
        print(f"Успешно добавихте числото {number} към list_C!")

list_C = list(set(list_C))
print("Премахнахте дубликатите от list_C!")

list_C = sorted(list_C, key=abs, reverse=True)
print("Сортирахте list_C по абсолютна стойност в намаляващ ред.")

