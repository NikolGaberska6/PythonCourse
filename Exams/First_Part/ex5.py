import random

while True:
  p = int(input("Въведете число в интервала: (8 < p < 25): "))
  if 8 < p < 25:
    break
  else:
    print("Моля въведете число в посочения интервал!")

first_A = []
r1 = random.randint(-1500, -500)
r2 = random.randint(500, 2000)
print(f"Диапазона на числата е от {r1} до {r2}!")

while len(first_A) < p:
    number = int(input(f"Въведете число в диапазона: {r1} : {r2}: "))
    if r1 < number < r2:
        first_A.append(number)

num_2digits_divided_by_6 = 0
for number in first_A:
    if 10 <= number <= 99 or -99 <= number <= -10:
        if number % 6 == 0:
            num_2digits_divided_by_6 += 1
if num_2digits_divided_by_6 != 0:
 print(f"Броят на двуцифрените числа, кратни на 6 в листа са: {num_2digits_divided_by_6}")
else:
    print("Няма двуцифрени числа, кратни на 6 в листа!")

multiplication_sum = 1
for number in first_A:
    if -9 <= number <= -1:
        multiplication_sum *= number
if multiplication_sum != 1:
    print(f"Произведението на всички едноцифрени отрицателни числа е: {multiplication_sum}")
else:
    print("Няма едноцифрени, отрицателни числа в листа!")

second_B = []
for number in first_A:
    if abs(number) % 10 == 3 or abs(number) % 10 == 7:
        second_B.append(number)
        print(f"Добавихте {number} във втория лист.")

positive_nums_at_even_index = 0
for idx in range(len(second_B)):
    if idx % 2 == 0:
        if second_B[idx] > 0:
            positive_nums_at_even_index += 1
if positive_nums_at_even_index != 0:
    print(f"Броят на положителните елемнти на четни индекси са: {positive_nums_at_even_index}")
else:
    print("Няма положителни елементи на четни индекси в листа!")

for idx in range(len(second_B)):
    if second_B[idx] > 100:
        print(f"Заменихте числото {second_B[idx]} с -1.")
        second_B[idx] = -1

if len(second_B) > len(first_A):
    second_B = second_B[:-2]
    print("Премахнахте последните два елемента от листа!")
    # second_B.pop()
    # second_B.pop()