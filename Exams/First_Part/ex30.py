import random

while True:
    p = int(input("Въведете число в интервала (10 < p < 30): "))
    if 10 < p < 30:
        break
    else:
        print("Моля въвдете число в посочения интервал!")

list_L = []
r1 = random.randint(-999, -111)
r2 = random.randint(111, 999)
for i in range(p):
    number = random.randint(r1, r2)
    list_L.append(number)
    print(f"Добавихте числото {number} в интервала.")

sum_1digit_negative_numbers = 1
for number in list_L:
    if -9 <= number <= -1:
        sum_1digit_negative_numbers *= number
if sum_1digit_negative_numbers != 1:
    print(f"Произведението на всички едноцифрени отрицателни числа е: {sum_1digit_negative_numbers}.")
else:
    print("В листа няма едноцифрени отицателни числа!")

count_even_3digits = 0
for number in list_L:
    if 100 <= abs(number) <= 999:
        if abs(number) % 2 == 0:
            count_even_3digits +=1
if count_even_3digits != 0:
    print(f"Броя на числата, които са четни и трицифрени е: {count_even_3digits}.")
else:
    print("Няма четни трицифрени числа в листа!")

list_L2 = []
for number in list_L:
    if number % 5 == 0:
        list_L2.append(number)
        print(f"Добавихте числото {number} в листа.")

for idx in range(len(list_L2)):
    if idx % 4 == 0:
        print(f"Заменихте числото на индекс {idx} с 0.")
        list_L2[idx] = 0

if len(list_L2) > len(list_L):
    list_L2.pop(-1)
    list_L2.pop(-1)
    print("Изтрихте последните два елемента на списъка list_L2.")
elif len(list_L) > len(list_L2):
    print("Списъкът list_L е по-дълъг от списъкът list_L2.")
else:
    print("Двата списъка са с еднаква дължина!")