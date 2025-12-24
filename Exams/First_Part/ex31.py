import sys

while True:
    m = int(input("Въведете число в интервала: (25 ≤ m ≤ 70): "))
    if 25 <= m <= 70:
        break
    else:
        print("Моля въведете число в посочения интервал: ")

arr = []
while len(arr) < m:
    number = int(input("Въведете число в интервала [-5000, 5000]: "))
    if -5000 <= number <= 5000:
        arr.append(number)
        print(f"Добавихте числото '{number}' в листа!")
    else:
        print("Моля въведете число в посочения интервал!")

count_numbers_digit3 = 0
for number in arr:
    digit_decimal = (abs(number) // 10) % 10
    if digit_decimal == 3:
            count_numbers_digit3 += 1
if count_numbers_digit3 != 0:
    print(f"Броя на числата, които имат цифра на десетиците = 3 е: {count_numbers_digit3}.")
else:
    print("Няма числа е листа, които имат цифра на десетиците = 3.")

min_number = sys.maxsize
for number in arr:
    if number > 0 and number % 2 == 0:
        if number < min_number:
            min_number = number
if min_number == sys.maxsize:
    print("Няма положително четно число!")
else:
    print(f"Минималното четно положително число е: '{min_number}'.")

arr2 = []
for number in arr:
    str_number = str(abs(number))
    if str_number == str_number[::-1]:
        arr2.append(number)

for idx in range(len(arr2)):
    if idx % 2 != 0:
        print(f"Заменихте числото '{arr2[idx]}' с 999.")
        arr2[idx] = 999

if len(arr) == len(arr2):
    arr2.reverse()
    print("Обърнахте списъка arr2!")
else:
    print("Списъците не са с еднаква дължина!")

