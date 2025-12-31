import random

while True:
    p = int(input("Въведете число в посочения интервал (15 < p < 35): "))
    if 15 < p < 35:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_L = []
r1 = random.randint(-888, -111)
r2 = random.randint(111, 888)
for i in range(p):
    number = random.randint(r1, r2)
    list_L.append(number)
    print(f"Добавихте числото '{number}' към списъка с числа.")

multiply_positive_1digit_nums = 1
for number in list_L:
    if 1 <= number <= 9:
        multiply_positive_1digit_nums *= number
if multiply_positive_1digit_nums != 1:
    print(f"Произведението на всички едноцифрени положителни числа е: "
          f"'{multiply_positive_1digit_nums}'.")
else:
    print("Няма едноцифрени положителни числа в списъка!")

count_odd_3digits = 0
for number in list_L:
    if number % 2 != 0:
        if 100 <= abs(number) <= 999:
            count_odd_3digits +=1
if count_odd_3digits != 0:
    print(f"Броя на числата, които са нечетни и трицифрени е: '{count_odd_3digits}'.")
else:
    print("Няма нечетни трицифрени числа в листа!")

list_L2 = []
for number in list_L:
    if number % 7 == 0:
        list_L2.append(number)

for idx in range(len(list_L2)):
    if idx % 3 == 0:
        print(f"Заменихте числото {list_L2[idx]} с -1.")
        list_L2[idx] = -1

if len(list_L2) > len(list_L):
    list_L2 = list_L2[2:]
    print("Изтрихте първите два елемента от лист list_L2.")
elif len(list_L) > len(list_L2):
    print("Дължината на list_L е по-голяма от list_L2.")
else:
    print("Двата листа имат еднаква дължина!")
