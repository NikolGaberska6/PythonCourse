import random

while True:
  m = int(input("Въведете число в интервала (18 < m < 65): "))
  if 18 < m < 65:
      break
  else:
      print("Моля въведете число в посочения интервал!")

list_1 = []
for i in range(m):
    number = random.randint(-500, 500)
    list_1.append(number)
    print(f"Добавихте числото {number} в листа!")

count_2digits_negative_del6 = 0
for number in list_1:
    if -99 <= number <= -10:
        if number % 6 == 0:
            count_2digits_negative_del6 += 1
if count_2digits_negative_del6 != 0:
    print(f"Броя на отрицателните, двуцифрени числа, кратни на 6 е: {count_2digits_negative_del6}")
else:
    print("В листа няма отрицателни, двуцифрени числа, кратни на 6!")

list_C = []
for number in list_1:
    if number % 2 == 0 and number > 100:
        list_C.append(number)
        print(f"Добавихте {number} в листа.")

for idx in range(2, len(list_C), 3):
    list_C[idx] = -5

if len(list_1) > len(list_C):
    list_1.pop(-1)
    list_1.pop(-1)
    print("Премахнахте последните 2 елемента от list_1.")
elif len(list_C) > len(list_1):
    list_C.pop(-1)
    list_C.pop(-1)
    print(f"Премахнахте последните два елемента от list_C.")
else:
    print("Двата списъка са с равна дължина!")




