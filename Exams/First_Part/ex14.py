import random

try:
    while True:
     n = int(input("Въведете число в интервала (15 <= n <= 45): "))
     if 15 <= n <= 45:
        break
     else:
        print("Моля въедете число в посочения интервал!")
except:
    print("Моля въведете валидни данни!")

list_A = []
while len(list_A) < n:
    number = int(input("Въведете число в интервала: -3000 : 5000"))
    if -3000 <= number <= 5000:
        list_A.append(number)

sum_negative_even_digit = 0
for number in list_A:
    if number < 0:
        digit_of_decimal = (abs(number) // 10) % 10
        if digit_of_decimal % 2 == 0:
            sum_negative_even_digit += number
if sum_negative_even_digit != 0:
    print("Сумата на елементите, които са отрицателни и имат четна цифра"
          f"на десетиците е: {sum_negative_even_digit}")
else:
    print("В листа няма отрицателни елементи с четна цифра на десетиците!")

count_elements_two_digits_end_3 = 0
sum_elements_two_digits_end_3 = 0
for number in list_A:
    if 10 <= abs(number) <= 99:
        last_digit = abs(number) % 10
        if last_digit == 3:
            count_elements_two_digits_end_3 += 1
            sum_elements_two_digits_end_3 += number
if count_elements_two_digits_end_3 != 0:
    average = sum_elements_two_digits_end_3 / count_elements_two_digits_end_3
    print(f"Средно-аритметично на елементите, които са двуцифрени и завършват"
          f" на 3 е {average}")
else:
    print("Няма елементи в листа, които да са двуцифрени и да завършват на 3!")

list_B = []
for number in list_A:
    if number % 4 == 0 and number > 0:
        list_B.append(number)
        print(f"Добавихте числото {number} във втория лист.")

if len(list_A) > len(list_B):
    list_A = list_A[2:]
elif len(list_B) > len(list_A):
    for number in list_A:
        if 1 <= abs(number) <= 9:
            list_B.append(number)
            print(f"Добавихте {number} във втория лист.")