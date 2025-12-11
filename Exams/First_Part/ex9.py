import random

while True:
  z = int(input("Въведете число е интервала (25 < z < 100): "))
  if 25 < z < 100:
     break
  else:
     print("Моля въведете число в получения интервал!")

first_P = []
r1 = random.randint(-4200, -2000)
r2 = random.randint(1000, 3500)
while len(first_P) < z:
    number = int(input(f"Въведете число в интервала: {r1} : {r2} : "))
    if r1 < number < r2:
        first_P.append(number)
    else:
        print("Моля въведете число в посочения интервал!")

count_3digits_end0 = 0
for number in first_P:
    if number % 10 == 0 and 100 <= abs(number) <= 999:
        count_3digits_end0 += 1
if count_3digits_end0 != 0:
    print(f"Броя на числата, които са трицфрени и завършват на 0 е {count_3digits_end0}")
else:
    print("В листа няма числа, които са трицифрени и завършват на 0!")

count_negative_even_nums = 0
sum_negative_even_nums = 0
for number in first_P:
    if number % 2 == 0 and number < 0:
        count_negative_even_nums += 1
        sum_negative_even_nums += number
if count_negative_even_nums != 0:
 average = sum_negative_even_nums/count_negative_even_nums
 print(f"Средно аритметично на отрицателните, четни числа е: {average}.")
else:
    print("Няма четни, отрицателни числа в листа!")

second_P2 = []
for number in first_P:
    if number % 15 == 0:
        second_P2.append(number)
        print(f"Добавихте числото {number} във втория лист.")

count_numbers_contains_3 = 0
for number in second_P2:
    n = abs(number)
    while n > 0:
        last_digit = n % 10 #взимаме последната цифра
        if last_digit == 3: #проверяваме дали е равна на 3
            count_numbers_contains_3 += 1 #ако е 3 значи числото съдържа 3 и цикъла приключва
            break
        n = n // 10 #премахваме последната цифра
if count_numbers_contains_3 != 0:
    print(f"Броят на числата, съдържащи цифрата 3 е: {count_numbers_contains_3}")
else:
    print("В листа няма числа, съдържаши цифрата 3!")

for idx in range(len(second_P2)):
    if second_P2[idx] < 0:
        print(f"Заменихте числото {second_P2[idx]} с 33.")
        second_P2[idx] = 33

if len(first_P) > len(second_P2):
    if len(first_P) % 2 != 0: #нечетна дължина
        mid_element = len(first_P)//2 #индекса на средния елемент
        first_P.pop(mid_element) #премахване по индекс
        print("Премахнахте средния елемент на листа!")
    else: #четна дължина
        mid_element1 = len(first_P)//2 - 1 #левия елемент
        mid_element2 = len(first_P)//2 #десния елемент
        first_P.pop(mid_element2) #първо премахваме десния елемент!
        first_P.pop(mid_element1)
        print("Премахнахте двата средни елемента на листа!")
elif len(second_P2) > len(first_P):
    if len(second_P2) % 2 != 0:
        mid_element = len(second_P2)//2
        second_P2.pop(mid_element)
        print("Премахнахте средния елемент на листа!")
    else:
        mid_element1 = len(second_P2)//2 - 1 #левия елемент
        mid_element2 = len(second_P2)//2  #десния елемент
        second_P2.pop(mid_element2) #първо премахваме десния елемент!
        second_P2.pop(mid_element1)
        print("Премахнахте двата средни елемента на листа!")




