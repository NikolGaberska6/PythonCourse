import random

while True:
  q = int(input("Въведете число в диапазона (18 < q < 55): "))
  if 18 < q < 55:
     break
  else:
     print("Моля въведете число в дадения диапазон!")

r1 = random.randint(-1200, -600)
r2 = random.randint(300, 1800)
first_X = []

while len(first_X) < q:
    number = int(input(f"Въведете число в диапазона: {r1} : {r2} : "))
    if r1 < number < r2:
        first_X.append(number)
    else:
        print("Моля въведете число в дадения диапазон!")

sum_digit5 = 0
for number in first_X:
    if number % 10 == 5:
        sum_digit5 += number
if sum_digit5 != 0:
    print(f"Сумата на числата, чиято единична цифра е 5 е {sum_digit5}")
else:
    print("Няма числа, чиято единична цифра е 5 в листа!")

num_negative_2digits_nums = 0
for number in first_X:
    if number < 0 and -99 <= number <= -10:
        num_negative_2digits_nums += 1
if num_negative_2digits_nums != 0:
    print(f"Броят на отрицателните, двуцифрени числа е: {num_negative_2digits_nums}")
else:
    print("Няма отрицателни, двуцифрени числа в листа!")

second_X2 = []
for number in first_X:
    if number > 0 and number % 12 == 0:
        second_X2.append(number)
        print(f"Добавихте числото {number} във втория лист.")
if len(second_X2) == 0:
    print("Няма положителни и кратни на 12 за добавяне в листа.")

num_elements_even_idx_bigger_than_100 = 0
for idx in range(len(second_X2)):
    if idx % 2 == 0:
        if second_X2[idx] > 100:
            num_elements_even_idx_bigger_than_100 += 1
if num_elements_even_idx_bigger_than_100 != 0:
    print(f"Броят на елементите, които са по-големи от 100 и стоят на"
          f" четен индекс са {num_elements_even_idx_bigger_than_100}")
else:
    print("Няма елементи по-големи от 100 на четен индекс във втория лист!")

for idx in range(len(second_X2)):
    if second_X2[idx] < 50:
        print(f"Заменихте числото {second_X2[idx]} с 50.")
        second_X2[idx] = 50

if len(second_X2) > len(first_X):
    second_X2 = second_X2[:-2]
    print("Премахнахте последните 2 елемента от листа!")
