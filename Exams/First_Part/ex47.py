import random

while True:
    try:
        n = int(input("Въведете цяло число в интервала (30 < n < 80): "))
        if 30 < n < 80:
            break
        else:
            print("Моля въведете число в посочения интервал!")
    except  ValueError:
        print("Моля въведете валидни данни!")

nums = []
x = random.randint(-10000, -5000)
y = random.randint(5000, 10000)
for i in range(n):
    number = random.randint(x,y)
    nums.append(number)
    print(f"Добавихте числото {number} в листа!")

count_neg_end7_3 = 0
for number in nums:
    if number < 0:
        last_digit = abs(number) % 10
        if last_digit == 3 or last_digit == 7:
            count_neg_end7_3 += 1
if count_neg_end7_3 != 0:
    print(f"Броя на числата, които са отрицателни и завършват на цифра 3 или 7 е: {count_neg_end7_3}.")
else:
    print("Няма числа в листа, които да са отрицателни и да завършват на 3 или 7!")

sum_all_positive_3digits_nums = 0
for number in nums:
    if 100 <= number <= 999:
        sum_all_positive_3digits_nums += number
if sum_all_positive_3digits_nums != 0:
    print(f"Сумата на всички трицифрени положителни числа е: {sum_all_positive_3digits_nums}.")
else:
    print("Няма трицифрени положителни числа в листа!")

nums2 = []
for number in  nums:
    if number % 9 == 0:
        if abs(number) >= 10000:
            nums2.append(number)
            print(f"Добавихте числото {number} към втория списък!")

count_negative_num_even_index = 0
for idx in range(len(nums2)):
    if idx % 2 == 0:
        if nums2[idx] < 0:
            count_negative_num_even_index += 1
if count_negative_num_even_index != 0:
    print(f"Броя на отрицателните числа в nums2, които се намират на четни индекси е: {count_negative_num_even_index}.")
else:
    print("Няма отрицателни числа на четни индекси в nums2!")

for idx in range(len(nums2)):
    if idx % 5 == 0:
        print(f"Заменихте числото {nums2[idx]} с 500.")
        nums2[idx] = 500

if len(nums) > len(nums2):
    nums.pop(-1)
    print("Премахнахте последния елемент на nums.")
elif len(nums2) > len(nums):
    nums2.pop(-1)
    print("Премахнахте последния елемент на nums2.")
else:
    print("Списъците са с еднаква дължина!")

