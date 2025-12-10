import random
while True:
  try:
    m = int(input("Въведете числото m в интервала (20 < m < 70): "))
    if 20 < m < 70:
        break
    else:
        print("Моля въведете число в дадения интервал!")
  except:
    print("Невалидни данни!")
    print("Моля опитайте отново!")

x = random.randint(-5000, -1000) #-1000
y = random.randint(2000, 6000) #1000
print(f"Интервалът за въвеждане на числата е: {x} : {y}")
nums_1 = []

while len(nums_1) < m:
    num = int(input("Въведете число в интервала (x:y): "))
    if x <= num <= y:
        nums_1.append(num)
    else:
        print("Числото е извън интервала!")
        print("Моля опитайте отново!")

print("Листът от числа е: ")
print(*nums_1)

count_pos_even_nums = 0
for number in nums_1:
    last_digit = number % 10
    if number > 0 and last_digit % 2 == 0:
        count_pos_even_nums += 1
if count_pos_even_nums == 0:
    print("Няма намерени положителни, четни числа")
else:
    print(f"Броят на положителните, четни числа в листа е: {count_pos_even_nums}")

sum_negative_3digit_nums = 0
for number in nums_1:
    if -999 <= number <= -100:
        sum_negative_3digit_nums += number
if sum_negative_3digit_nums == 0:
    print("Няма намерени отрицателни, трицифрени числа!")
else:
    print(f"Сумата на всияки отрицателни трицифрени числа е: {sum_negative_3digit_nums}")

nums_2= []
numbers_4digits_del7 = 0
for number in nums_1:
    if number % 7 == 0 and abs(number) >= 1000:
        nums_2.append(number)
        numbers_4digits_del7 += 1
if numbers_4digits_del7 == 0:
    print("Няма намерени поне 4 цифрени и кратни на 7 числа в листа!")
print("Вторият лист от числа с поне 4 цифрени елементи кратни на 7: ")
print(*nums_2)

num_negative_even_index = 0
for idx in range(len(nums_2)):
    if idx % 2 == 0:
        number = nums_2[idx]
        if number < 0:
            num_negative_even_index += 1
if num_negative_even_index == 0:
    print("Няма намерени отрицателни елементи на четен индекс в листа!")
else:
    print(f"Броя на отрицателните елементи на четен индекс в листа са: {num_negative_even_index}")

nums_index_del3 = 0
for idx in range(len(nums_2)):
    if idx % 3 == 0:
        nums_2[idx] = 100
        nums_index_del3 +=1
if nums_index_del3 == 0:
   print("Няма елементи в листа, на индекси кратни на 3!")

print(f"Дължината на първия списък: {len(nums_1)}")
print(f"Дължината на втория списък: {len(nums_2)}")

if len(nums_1) != len(nums_2):
    if len(nums_1) > len(nums_2):
        print("Дължината на първия лист е по голяма!")
        mid_index = len(nums_1) // 2 #намира индекса на средния елемент
        element_for_remove = nums_1[mid_index]
        print(f"Премахнахте елемента {element_for_remove}")
        nums_1.pop(mid_index) #pop премахва елемента по индекс, докато remove премахва по стойност
    elif len(nums_2) > len(nums_1):
        print("Дължината на втория лист е по голяма!")
        mid_index = len(nums_2) // 2
        element_for_remove = nums_2[mid_index]
        print(f"Премахнахте елемента {element_for_remove}")
        nums_2.pop(mid_index)
    else:
        print("Дължините на двата списъка са равни!")

