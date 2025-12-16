import random

while True:
 p = int(input("Въведете число в интервала (14 ≤ p ≤ 90): "))
 if 14 <= p <= 90:
     break
 else:
     print("Моля въведете число в посочения интервал!")

list_X = []
for i in range(p):
    number = random.randint(-8888, 8888)
    list_X.append(number)
    print(f"Добавихте числото {number} към листа list_X.")

count_reversed_num = 0
for number in list_X:
    reversed_num = "".join(reversed(str(number))) #правим го string, reversed и го правим с join за да го върне като низ
    if reversed_num == str(number):
        count_reversed_num += 1
if count_reversed_num != 0:
    print(f"Броя на числата, които са огледални е: {count_reversed_num}.")
else:
    print("В листа няма огледани числа.")

# for n in numbers:
#    if str(n) == str(n)[::-1]: ---> взима вс елементи в обратен ред
#        count += 1

sum_3digit_del_5 = 0
for number in list_X:
    if 100 <= abs(number) <= 999:
        if abs(number) % 5 == 0:
            sum_3digit_del_5 += number
if sum_3digit_del_5 != 0:
    print(f"Сумата на всички тризначни числа, които са кратни на 5: {sum_3digit_del_5}")
else:
    print("Няма тризначни числа, кратни на 5 в листа!")

list_Y = []
for number in list_X:
    str_number = str(abs(number))
    if "7" in str_number:
     list_Y.append(number)
     print(f"Добавихте {number} във втория лист.")

for idx in range(len(list_Y)):
    sum_of_digits = 0
    if idx % 4 == 0:
        number_at_index = list_Y[idx]
        for i in str(abs(number_at_index)):
            sum_of_digits += int(i)
        list_Y[idx] = sum_of_digits

if len(list_X) < len(list_Y):
    for number in list_Y:
        if number < 0:
            list_X.append(number)
            print(f"Добавихте {number} в list_X.")