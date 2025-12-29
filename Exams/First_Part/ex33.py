import random

while True:
 try:
    n = int(input("Въведете число в интервала (25 < n < 65): "))
    if 25 < n < 65:
        break
    else:
        print("Моля въведете число в посочения интервал!")
 except:
     print("Моля въведете валидни данни!")

list_A = []
r1 = random.randint(-7000, -1000)
r2 = random.randint(2000, 8000)
for i in range(n):
    number = random.randint(r1, r2)
    list_A.append(number)
    print(f"Добавихте числото '{number}' в list_A.")

count_positive_nums_ending5 = 0
for number in list_A:
    if number > 0:
        last_digit = number % 10
        if last_digit == 5:
            count_positive_nums_ending5 += 1
if count_positive_nums_ending5 != 0:
    print(f"Броя на положителните числа, които завършват на 5 е: {count_positive_nums_ending5}.")
else:
    print("Няма числа в списъка, които да са положителни и да завършват на 5!")

sum_3digit_positive_nums = 0
for number in list_A:
    if 100 <= number <= 999:
        sum_3digit_positive_nums += number
if sum_3digit_positive_nums != 0:
    print(f"Сумата на всички трицифрени положителни числа e: {sum_3digit_positive_nums}.")
else:
    print("Няма трицифрени положителни числа в списъка!")

list_B = []
for number in list_A:
    if abs(number) % 6 == 0: #при кратност не е задължително abs
        list_B.append(number)
        print(f"Добавихте числото {number} в списък list_B.")

count_elements_at_even_idx = 0
for idx in range(len(list_B)):
    if idx % 2 == 0:
        count_elements_at_even_idx += 1
if count_elements_at_even_idx != 0:
    print(f"Броя на елементите в B, които са на четен индекс е: {count_elements_at_even_idx}.")
else:
    print("Няма елементи в В, които да са на четен идекс.")

for idx in range(len(list_B)):
    if list_B[idx] < -1000:
        print(f"Заменихте числото {list_B[idx]} s 100.")
        list_B[idx] = 100

if len(list_A) > len(list_B):
    list_A.pop(0)
    print("Премахнахте първия елемент на list_A.")
elif len(list_B) > len(list_A):
    list_B.pop(0)
    print("Премахнахте първия елемент на list_B.")
else:
    print("Двата листа са с еднаква дължина.")