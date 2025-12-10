import random

while True:
 t = int(input("Въведете число в интервала (12 < t < 60): "))
 if 12 < t < 60:
     break
 else:
     print("Моля въведете число в дадения интервал!")

first_S = []
a = random.randint(-999, -111)
b = random.randint(222, 999)

while len(first_S) < t:
    number = int(input(f"Въведете число в интервала: {a} : {b} : "))
    if a < number < b:
        first_S.append(number)
    else:
        print("Моля въведете число в дадения интервал!")

num_even_numbers_end_4 = 0
for number in first_S:
    if number % 2 == 0 and abs(number) % 10 == 4:
        num_even_numbers_end_4 += 1
if num_even_numbers_end_4 != 0:
    print(f"Броя на четните числа, завършващи на 4 са: {num_even_numbers_end_4}.")
else:
    print("Няма четни числа, завършващи на 4 в листа.")

num_elements_with3_digits = 0
sum_elements_with3_digits = 0
for number in first_S:
    if 100 <= number <= 999 or -999 <= number <= -100:
        num_elements_with3_digits += 1
        sum_elements_with3_digits += number
if num_elements_with3_digits != 0:
    average = sum_elements_with3_digits/num_elements_with3_digits
    print(f"Средно аритметично на елементите, които имат точно 3 цифри e {average}.")
else:
    print("В листа няма елементи, които имат точно 3 цифри!")

second_S2 = []
for number in first_S:
    if number % 4 == 0 or number % 8 == 0:
        second_S2.append(number)
        print(f"Добавихте {number} към втория лист.")

num_negative_elements_with_even_idx = 0
for idx in range(len(second_S2)):
    if idx % 2 == 0:
        if second_S2[idx] < 0:
            num_negative_elements_with_even_idx += 1
if num_negative_elements_with_even_idx != 0:
    print(f"Броя на елементите, които са по-малки от 0 и имат четен "
          f"индекс е: {num_negative_elements_with_even_idx}")
else:
    print("Няма елементи, които са по малки от 0 и имат четен индекс в листа!")

for idx in range(len(second_S2)):
    if second_S2[idx] > 500:
        print(f"Сменихте числото {second_S2[idx]} с 500.")
        second_S2[idx] = 500

if len(first_S) > len(second_S2):
    while len(first_S) != len(second_S2):
        second_S2.append(0)
elif len(second_S2) > len(first_S):
    while len(second_S2) != len(first_S):
        first_S.append(0)