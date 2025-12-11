import random
while True:
  c = int(input("Въведете число в интервала (10 < с < 45): "))
  if 10 < c < 45:
     break
  else:
     print("Моля въведете число в посочения интервал: ")

first_R = []
r1 = random.randint(-700, -400)
r2 = random.randint(400, 900)

while len(first_R) < c:
    number = int(input(f"Въведете число в диапазона {r1} : {r2} : "))
    if r1 < number < r2:
        first_R.append(number)
    else:
        print("Моля въведете число в посочения диапазон!")

count_1digits_even = 0
for number in first_R:
    if number % 2 == 0 and 1 <= abs(number) <= 9:
        count_1digits_even += 1
if count_1digits_even != 0:
    print(f"Броя на едноцифрените четни числа в листа е: {count_1digits_even}")
else:
    print("Няма едноцифрени четни числа в листа!")

multiplication_sum = 1
for number in first_R:
    digit_of_100 = (abs(number) // 100) % 10
    if digit_of_100 % 2 != 0:
        multiplication_sum *= number
if multiplication_sum != 1:
    print(f"произведението на всички числа, чиято цифра на "
          f"стотиците е нечетна e: {multiplication_sum}")
else:
    print("Нама числа, чиято цифра на стотиците да е нечетна в листа!")

second_R2 = []
for number in first_R:
    if number % 5 == 0:
        second_R2.append(number)
        print(f"Добавихте числото {number} към втория лист.")

count_positive_odd_index = 0
for idx in range(len(second_R2)):
    if idx % 2 != 0:
        if second_R2[idx] > 0:
            count_positive_odd_index += 1
if count_positive_odd_index != 0:
    print(f"Броя на числата, които са положителни и с нечетен индекс е: {count_positive_odd_index}")
else:
    print("Няма числа в листа, които да са положителни и с нечетен индекс!")

for idx in range(len(second_R2)):
    if abs(second_R2[idx]) % 10 == 9:
        print(f"Заменихте числото {second_R2[idx]} с 0.")
        second_R2[idx] = 0

if len(first_R) < len(second_R2):
    print("Дължината на първия лист е по-малка от дължината на втория.")
    first_R.append(-2)
    first_R.append(-2)
else:
    print("ДЪлжината на двата листа са равни!")
