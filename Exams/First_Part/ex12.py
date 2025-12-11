import random

while True:
  r = int(input("Въведете число в интервала (16 < r < 42): "))
  if 16 < r < 42:
     break
  else:
     print("Моля въведете число в зададения интервал!")

first_M = []
r1 = random.randint(-2400, -1000)
r2 = random.randint(200, 1400)

while len(first_M) < r:
    number = int(input(f"Въведете число в интервала {r1} : {r2} : "))
    if r1 < number < r2:
        first_M.append(number)
    else:
        print("Моля въведете число в посочения интервал!")

count_negative_2digits_even_last_digit = 0
for number in first_M:
    if -99 <= number <= -10:
        last_digit = abs(number) % 10
        if last_digit % 2 == 0:
            count_negative_2digits_even_last_digit += 1
if count_negative_2digits_even_last_digit != 0:
    print("Броя на отрицателните двуцифрени числа, които завършват "
          f"на четна цифра е {count_negative_2digits_even_last_digit}")
else:
    print("В листа няма отрицателни двуцифрени числа, които завършват на четна цифра!")

count_3digits_positive_numbers = 0
sum_3digits_positive_numbers = 0
for number in first_M:
    if 100 <= number <= 999:
        count_3digits_positive_numbers += 1
        sum_3digits_positive_numbers += number
if count_3digits_positive_numbers != 0:
    average = sum_3digits_positive_numbers/count_3digits_positive_numbers
    print(f"Средно на всички трицфрени положителни числа е {average}")
else:
    print("Няма трицифрени положителни числа в листа!")

second_M2 = []
for number in first_M:
    if number % 3 == 0:
        second_M2.append(number)
        print(f"Добавихте {number} във втория лист!")

count_odd_elements_even_idx = 0
for idx in range(len(second_M2)):
    if idx % 2 == 0:
        if second_M2[idx] % 2 != 0:
            count_odd_elements_even_idx += 1
if count_odd_elements_even_idx != 0:
    print(f"Брой на елементите, които са нечетни и стоят на "
          f"четни позиции е {count_odd_elements_even_idx}")
else:
    print("В листа няма нечетни елементи на четни позиции!")

for idx in range(len(second_M2)):
    if second_M2[idx] < -1000:
        print(f"Заменихте числото {second_M2[idx]} с -1000.")
        second_M2[idx] = -1000

if len(first_M) == len(second_M2):
    first_M[:3], second_M2[:3] = second_M2[:3], first_M[:3]
    print("Разменихте първите три елемента на листовете.")
else:
    print("Дължините на двата листа са различни!")

