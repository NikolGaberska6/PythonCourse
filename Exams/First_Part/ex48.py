import random

while True:
    try:
        n = int(input("Въведете число в интервала (25 < n < 70): "))
        if 25 < n < 70:
            break
        else:
            print("Моля въведете число в посочения интервал!")
    except ValueError:
        print("Моля въведете валидни данни!")

x = random.randint(-7000, -2000)
y = random.randint(3000, 8000)
nums = []
for i in range(n):
    number = random.randint(x, y)
    nums.append(number)
    print(f"Успешно добавихте числото {number} в списъка!")

count_positive_end5_or0 = 0
for number in nums:
    if number > 0:
        last_digits = number % 10
        if last_digits == 5 or last_digits == 0:
            count_positive_end5_or0 += 1
if count_positive_end5_or0 != 0:
    print(f"Броя на числата, които са положителни и завършват на цифра 5 или 0 е: {count_positive_end5_or0}.")
else:
    print("Няма положителни числа в листа, които да завършват на 5 или 0!")

sum_all_negative_3digits_nums = 0
for number in nums:
    if -999 <= number <= -100:
        sum_all_negative_3digits_nums += number
if sum_all_negative_3digits_nums != 0:
    print(f"Сумата на всички трицифрени отрицателни числа е: {sum_all_negative_3digits_nums}")
else:
    print("Няма трицифрени отрицателни числа в листа!")

nums_2 = []
for number in nums:
    if number % 6 == 0:
        if abs(number) >= 1000:
            nums_2.append(number)
            print(f"Добавихте числото {number} във втория лист с числа!")

count_negative_nums_odd_index = 0
for idx in range(len(nums_2)):
    if idx % 2 != 0:
        if nums_2[idx] < 0:
            count_negative_nums_odd_index += 1
if count_negative_nums_odd_index != 0:
    print(f"Броя на отрицателните елементи в nums2, които се намират на нечетни индекси е: {count_negative_nums_odd_index}")
else:
    print("Няма отрицателни елементи на нечетни индекси в nums2!")

for idx in range(len(nums_2)):
    if idx % 4 == 0:
        print(f"Заменихте числото {nums_2[idx]} с 200!")
        nums_2[idx] = 200

if len(nums) > len(nums_2):
    if len(nums) % 2 != 0:
        middle_element = len(nums) // 2
        nums.pop(middle_element)
        print("Премахнахте средния елемент от листа nums!")
elif len(nums_2) > len(nums):
    if len(nums_2) % 2 != 0:
        middle_element = len(nums_2) // 2
        nums_2.pop(middle_element)
        print("Премахнахте средния елемент от листа nums_2!")
else:
    print("Двата списъка са с еднаква дължина!")