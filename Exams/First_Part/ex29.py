import random

while True:
  k = int(input("Въведете число в интервала (15 ≤ k ≤ 45): "))
  if 15 <= k <= 45:
      break
  else:
      print("Моля въведете число в посочения интервал!")

nums = []
r1 = random.randint(-1500, -500)
r2 = random.randint(500, 2500)
while len(nums) < k:
    number = int(input(f"Въведете число в интервала: {r1} : {r2} : "))
    if r1 < number < r2:
        nums.append(number)
    else:
        print("Моля въвдете число в посочения интервал!")

count_2digit_odd_nums = 0
for number in nums:
    if 10 <= abs(number) <= 99:
        if abs(number) % 2 != 0:
            count_2digit_odd_nums += 1
if count_2digit_odd_nums != 0:
    print(f"Броя на числата, които са двуцифрени и нечетни е: {count_2digit_odd_nums}")
else:
    print("Няма числа, които да са двуцифрени и нечети в листа!")

sum_of_nums_hundreds2 = 0
count_of_nums_hundreds2 = 0
for number in nums:
    digit_of_hundreds = (abs(number) // 100) % 10
    if digit_of_hundreds == 2:
        count_of_nums_hundreds2 += 1
        sum_of_nums_hundreds2 += number
if count_of_nums_hundreds2 != 0:
    average = sum_of_nums_hundreds2/count_of_nums_hundreds2
    print("Средно аритметично на числата, чиято цифра "
          f"на стотиците е 2 е: {average}.")
else:
    print("Няма числа в листа, чията цифра на стотиците да е 2!")

nums2 = []
for number in nums:
    str_number = str(number)
    for digit in str_number:
        if digit == "7":
            nums2.append(int(number))
            print(f"Добавихте числото {int(number)} в листа!")
            break

for idx in range(len(nums2)):
    num = nums2[idx]
    if num < 0:
        print(f"Заменихте числото {num} с 77.")
        nums2[idx] = 77

count_elements_at_even_index = 0
for idx in range(len(nums2)):
    if idx % 2 == 0:
        count_elements_at_even_index += 1
if count_elements_at_even_index != 0:
    print(f"Броя елементи на четен индекс е: {count_elements_at_even_index}")
else:
    print("В листа няма елементи на четен индекс!")

if len(nums2) < len(nums):
    while len(nums2) != len(nums):
        nums2.append(1)
    print("Изравнихте дължините на двата списъка!")