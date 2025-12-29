import random

while True:
    t = int(input("Въведете число в интервала (18 < t < 55)"))
    if 18 < t < 55:
        break
    else:
        print("Моля въведете число в посочения интервал!")

list_S = []
r1 = random.randint(-3000, -1000)
r2 = random.randint(1000, 4000)
for i in range(t):
    number = random.randint(r1, r2)
    list_S.append(number)
    print(f"Добавихте числото {number} в списъка list_S.")

count_negative_del9 = 0
for number in list_S:
    if number < 0:
        if number % 9 == 0:
            count_negative_del9 += 1
if count_negative_del9 != 0:
    print(f"Броя на числата, които са кратни на 9 и отрицателни "
          f"е {count_negative_del9}.")
else:
    print("Няма отрицателни числа, кратни на 9 в листа!")

average = 0
sum_2digits = 0
count_2digits = 0
for number in list_S:
    if 10 <= abs(number) <= 99:
        sum_2digits += number
        count_2digits += 1
if count_2digits != 0:
    average = sum_2digits/count_2digits
    print(f"Средно аритметично на всички двуцифрени числа е {average}.")
else:
    print("Няма двуцифрени числа в листа!")

list_S2 = []
for number in list_S:
    sum_of_digits = 0
    str_number = str(abs(number))
    for digit in str_number:
        int_digit = int(digit)
        sum_of_digits += int_digit
    if sum_of_digits % 2 == 0:
        list_S2.append(number)
        print(f"Добавихте числото {number} към list_S2.")

for idx in range(len(list_S2)):
    current_num = list_S2[idx]
    if current_num > 500:
        print(f"Заменихте числото {current_num} с 500.")
        list_S2[idx] = 500

if len(list_S) > len(list_S2):
    list_S = list_S[3:]
    print("Премахнахте първите 3 елемента от list_S.")
elif len(list_S2) > len(list_S):
    list_S2 = list_S2[3:]
    print("Премахнахте първите 3 елемента от list_S2.")
else:
    print("Списъците са с еднаква дължина!")