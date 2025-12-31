import random

while True:
    t = int(input("Въведете число в интервала (20 < t < 60): "))
    if 20 < t < 60:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_S = []
r1 = random.randint(-2500, -500)
r2 = random.randint(500, 3500)

for i in range(t):
    number = random.randint(r1, r2)
    list_S.append(number)
    print(f"Добавихте числото {number} в списъка с числа!")

count_nums_positive_del7 = 0
for number in list_S:
    if number > 0 and number % 7 == 0:
        count_nums_positive_del7 += 1
if count_nums_positive_del7 != 0:
    print(f"Броя на числата, които са кратни на 7 и положителни е: {count_nums_positive_del7}.")
else:
    print("Няма числа в листа, които да са положтелни и кратни на 7!")

average = 0
sum_of_nums = 0
count_of_nums = 0
for number in list_S:
    if -99 <= number <= -10:
        sum_of_nums += number
        count_of_nums += 1
if count_of_nums != 0:
    average = sum_of_nums/count_of_nums
    print(f"Средно аритметично на всички двуцифрени отрицателни числа е: {average}.")
else:
    print("Няма двуцифрени отрицателни числа в листа!")

list_S2 = []
for number in list_S:
    sum_of_digits = 0
    str_number = str(abs(number))
    for element in str_number:
        sum_of_digits += int(element)
    if sum_of_digits % 2 != 0:
        list_S2.append(number)

for idx in range(len(list_S2)):
    if list_S2[idx] < -200:
        print(f"Заменихте числото {list_S2[idx]} с -200.")
        list_S2[idx] = -200

if len(list_S) > len(list_S2):
    list_S = list_S[:-4]
    print("Премахнахте последните 4 елемента от листа!")
elif len(list_S2) > len(list_S):
    list_S2 = list_S2[:-4]
    print("Премахнахте последните 4 елемента от листа!")
else:
    print("Дължините на двата листа са равни!")
