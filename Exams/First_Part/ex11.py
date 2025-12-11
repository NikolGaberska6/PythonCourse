import random

while True:
 w = int(input("Въведете число в диапазона: (22 < w < 80): "))
 if 22 < w < 80:
     break
 else:
     print("Моля въведете число в дадения диапазон!")

first_D = []
r1 = random.randint(-9999, -3000)
r2 = random.randint(2000, 8000)
while len(first_D) < w:
    number = int(input(f"Въведете число в диапазона {r1} : {r2} : "))
    if r1 < number < r2:
        first_D.append(number)
    else:
        print("Моля въведете число в посочения диапазон!")

count_numbers_with_digits_of1000 = 0
for number in first_D:
    digit_of_1000 = (abs(number) // 1000) % 10
    if digit_of_1000 == 3:
        count_numbers_with_digits_of1000 += 1
if count_numbers_with_digits_of1000 != 0:
    print(f"Броя на числата, чиято цифра на хилядите е 3 е: {count_numbers_with_digits_of1000}")
else:
    print("Няма числа, чиято цифра на хилядите да е 3 в листа!")

count_positive_2digits_nums = 0
sum_positive_2digits_nums = 0
for number in  first_D:
    if number > 0 and 10 <= number <= 99:
        count_positive_2digits_nums += 1
        sum_positive_2digits_nums += number
if count_positive_2digits_nums != 0:
    average = sum_positive_2digits_nums/count_positive_2digits_nums
    print(f"Средно на всички числа, които са положителни и двуцифрени e {average}")
else:
    print("Няма положителни, двуцифрени числа в листа!")

second_D2 = []
for number in first_D:
    if number % 4 == 0 and number % 6 == 0:
        second_D2.append(number)
        print(f"Добавихте {number} във втория лист.")

count_negative_elements_index_divided4 = 0
for idx in range(len(second_D2)):
    if idx % 4 == 0:
        if second_D2[idx] < 0:
            count_negative_elements_index_divided4 += 1
if count_negative_elements_index_divided4 != 0:
    print(f"Брой на елементите, които са отрицателни и на индекс "
          f"кратен на 4 e {count_negative_elements_index_divided4}")
else:
    print("Няма отрицателни елементи на индекс кратен на 4 в листа!")

for idx in range(len(second_D2)):
    if abs(second_D2[idx]) > 9999:
        print(f"Заменихте чилото {second_D2[idx]} с 4444.")
        second_D2[idx] = 4444

if len(first_D) > len(second_D2):
    first_D = first_D[2:-2]
elif len(second_D2) > len(first_D):
    second_D2 = second_D2[2:-2]
else:
    print("Дължините на двата списъка са равни!")