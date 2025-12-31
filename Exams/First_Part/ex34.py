import random

while True:
    k = int(input("Въведете число в интервала (10 ≤ k ≤ 40): "))
    if 10 <= k <= 40:
        break
    else:
        print("Моля въведете число в посочения интервал!")

nums = []
r1 = random.randint(-1200, -300)
r2 = random.randint(300, 2000)
for i in range(k):
    number = random.randint(r1, r2)
    nums.append(number)
    print(f"Добавихте числото {number} в списъка с числа!")

count_2digits_even = 0
for number in nums:
    if 10 <= abs(number) <= 99:
        if number % 2 == 0:
            count_2digits_even += 1
if count_2digits_even != 0:
    print(f"Броя на числата, които са двуцифрени и четни е: {count_2digits_even}")
else:
    print("Няма числа, които да са двуцифрени и четни в листа!")

count_nums_second_digit_5 = 0
sum_nums_second_digit_5 = 0
for number in nums:
    second_digit = (abs(number) // 10) % 10
    if second_digit == 5:
        count_nums_second_digit_5 += 1
        sum_nums_second_digit_5 += number
if count_nums_second_digit_5 != 0:
    average = sum_nums_second_digit_5 / count_nums_second_digit_5
    print(f"Средно аритметично на числата, чиято цифра на десетиците е 5 е: {average}.")
else:
    print("Няма числа в листа, чиято цифра на десетиците да е 5!")

nums2 = []
for number in nums:
    str_number = str(abs(number))
    for element in str_number:
        if element == "3":
            nums2.append(number)
            print(f"Добавихте числото {number} към втория списък с числа.")
            break

for idx in range(len(nums2)):
    if nums2[idx] < 0:
        print(f"Заменихте числото {nums2[idx]} с 33.")
        nums2[idx] = 33

count_elements_at_odd_idx = 0
for idx in range(len(nums2)):
    if idx % 2 != 0:
        count_elements_at_odd_idx += 1
if count_elements_at_odd_idx != 0:
    print(f"Броя на елементите на нечетен индекс е: {count_elements_at_odd_idx}")
else:
    print("Няма елементи на нечетен индекс в листа!")

if len(nums2) < len(nums):
    while len(nums2) != len(nums):
        nums2.append(0)
    print("Изравнихте дължините на двата листа!")
elif len(nums2) > len(nums):
    print("ДЪлжината на втория списък е по-голяма.")
else:
    print("Дължините на двата списъка са равни!")