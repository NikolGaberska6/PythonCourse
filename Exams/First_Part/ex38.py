import random

try:
 while True:
    n = int(input("Въведете число в интервала (15 < n < 60): "))
    if 15 < n < 60:
        break
    else:
        print("Моля въведете число в посочения интервал!")
except:
    print("Моля въведете валидни данни!")

a = random.randint(-3000, -500)
b = random.randint(1000, 4000)

arr = []
for i in range(n):
    number = random.randint(a, b)
    arr.append(number)
    print(f"Успешно добавихте числото {number} в списъка!")

count_negative_last_odd_digit = 0
for number in arr:
    if   number < 0:
        last_digit = abs(number) % 10
        if last_digit % 2 != 0:
            count_negative_last_odd_digit += 1
if count_negative_last_odd_digit != 0:
    print(f"Броя на числата, които са отрицателни и завършват на нечетна цифра е: '{count_negative_last_odd_digit}'.")
else:
    print("Няма отрицателни числа, които да завършват на нечетна цифра в листа!")

sum_2digit_positive_nums = 1
for number in arr:
    if 10 <= number <= 99:
        sum_2digit_positive_nums *= number
if sum_2digit_positive_nums != 1:
    print(f"Произведението на всички двуцифрени положителни числа е: {sum_2digit_positive_nums}.")
else:
    print("Няма двуцифрени положителни числа в листа!")

arr2 = []
for number in arr:
    if abs(number) >= 100:
        if number % 5 != 0:
            arr2.append(number)
            print(f"Числото {number} не е кратно на 5 и го добавихте в листа!")

sum_positive_el_odd_index = 0
count_positive_el_odd_index = 0
for idx in range(len(arr2)):
    if idx % 2 != 0:
        if arr2[idx] > 0:
            sum_positive_el_odd_index += arr2[idx]
            count_positive_el_odd_index += 1
if count_positive_el_odd_index != 0:
    average = sum_positive_el_odd_index/count_positive_el_odd_index
    print(f"Средноаритметичното на положителните елементи на нечетни индекси в arr2 е: '{average}'.")
else:
    print("Няма положителни елементи на нечетни индекси в листа!")

for idx in range(len(arr2)):
    if arr2[idx] < 0:
        print(f"Заменихте числото {arr2[idx]} с -1.")
        arr2[idx] = -1

if len(arr) == len(arr2):
    first_element_arr = arr[0]
    last_element_arr = arr[-1]
    arr[-1] = first_element_arr
    arr[0] = last_element_arr
    first_element_arr2 = arr2[0]
    last_element_arr2 = arr2[-1]
    arr2[-1] = first_element_arr2
    arr2[0] = last_element_arr2
    #  list1[0], list1[-1] = list1[-1], list1[0]
    #  list2[0], list2[-1] = list2[-1], list2[0]
    print("Разменете първия и последния елемент на списъците.")
else:
    print("Списъците са с различна дължина!")


    