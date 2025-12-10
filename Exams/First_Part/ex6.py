import random

while True:
 n = int(input("Въведете число в интервала (30 < n < 90): "))
 if 30 < n < 90:
     break
 else:
     print("Моя въведете число в посочения интервал!")

r1 = random.randint(-8000, -3000)
r2 = random.randint(1000, 5000)
first_L = []

while len(first_L) < n:
    number = int(input(f"Въведете число в диапазона {r1} : {r2}: "))
    if r1 < number < r2:
        first_L.append(number)
    else:
        print("Моля въведете число в посочения интервал!")

num_negative_del11 = 0
for number in first_L:
    if number < 0 and number % 11 == 0:
        num_negative_del11 += 1
if num_negative_del11 != 0:
    print(f"Броя на отрицателните числа, кратни на 11 e: {num_negative_del11}")
else:
    print("Няма отрицателни числа, кратни на 11 в листа!")

sum_positive_even_2digits_nums = 0
for number in first_L:
    if number > 0 and number % 2 == 0:
        if 10 <= number <= 99:
            sum_positive_even_2digits_nums += number
if sum_positive_even_2digits_nums != 0:
    print(f"Сумата от всички положителни, четни, двуцифрени числа "
          f"е: {sum_positive_even_2digits_nums}")
else:
    print("Няма положителни, четни, двуцифрени числа в листа!")

second_L2 = []
for number in first_L:
    if (abs(number) // 10) % 10 == 1 or (abs(number) // 10) % 10 == 2:
        second_L2.append(number)
        print(f"Добавихте {number} към втория лист с числа.")

num_odd_nums_odd_idx = 0
for idx in range(len(second_L2)):
    if idx % 2 != 0:
        if second_L2[idx] % 2 != 0:
            num_odd_nums_odd_idx += 1
if num_odd_nums_odd_idx != 0:
    print(f"Броя на нечетните числа на нечетни позиции в листа е: {num_odd_nums_odd_idx}")
else:
    print("Няма нечетни числа на нечетни позиции в листа.")

for idx in range(len(second_L2)):
    if second_L2[idx] < -5000:
        print(f"Заменихте числото {second_L2[idx]} с 5000.")
        second_L2[idx] = 5000

if len(first_L) > len(second_L2):
    first_L = first_L[3:]
    print("Изтрихте първите 3 елемента от първия списък.")
elif len(second_L2) > len(first_L):
    second_L2 = second_L2[3:]
    print("Изтрихте първите 3 елемента от втория списък.")






