import random
import sys

try:
    while True:
     p = int(input("Въведете число в интервала (12 <= p <= 55): "))
     if 12 <= p <= 55:
         break
     else:
         print("Моля въведете число в дадения интервал!")
except:
    print("Моля въведете валидни данни!")

data = []
for i in range(p):
    number = random.randint(-999, 999)
    data.append(number)

count_odd_2digits = 0
for number in data:
    if number % 2 != 0:
        if 10 <= abs(number) <= 99:
            count_odd_2digits += 1
if count_odd_2digits != 0:
    print(f"Броя на елементите, които са двуцифрени и нечетни е {count_odd_2digits}")
else:
    print("Няма елементи в листа, които да са деуцифрени и нечетни")

max_number = -sys.maxsize
for number in data:
    last_digit = abs(number) % 10
    if last_digit == 5:
        if number > max_number:
            max_number = number
print(f"Максималния елемент, чиято цифра на единиците е 5 е: {max_number}")

filtered = []
for number in data:
    if number % 9 == 0:
        filtered.append(number)
        print(f"Добавихте {number} към листа filtered.")

for number in filtered.copy():
    sum_of_digits = 0
    current_num = abs(number)
    while current_num > 0:
      last_digit = current_num % 10
      sum_of_digits += last_digit
      current_num = current_num // 10
    if sum_of_digits % 2 == 0:
        filtered.remove(number)
        print(f"Премахнахте числото {number} от списъка filtered.")

if len(data) > len(filtered):
    filtered.append(777)
elif len(filtered) > len(data):
    data.append(777)
else:
    print("Двата списъка имат еднаква дължина!")





