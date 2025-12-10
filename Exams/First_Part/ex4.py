import random

while True:
    k = int(input("Въведете цяло число в интервала (15 < k < 40): "))
    if 15 < k < 40:
        break
    else:
        print("Моля, въведете число в интервала!")

minN = random.randint(-300, -30)
maxN = random.randint(50, 300)
print(f"Интервалът на числата е от {minN} до {maxN}")
arr = []

while len(arr) < k:
    number = int(input(f"Въведете число в интервала {minN} : {maxN}: "))
    if minN < number < maxN:
        arr.append(number)
    else:
        print("Моля въведете число в дадения интервал!")

print("Вашият лист с числа е: ")
print(*arr)

count_positive_divided_by_five = 0
for number in arr:
    if number > 0:
      if (number // 100) % 10 > 5: #цифрата на стотиците дали е > 5
         count_positive_divided_by_five += 1
if count_positive_divided_by_five == 0:
    print("Няма положителни числа, чиято цифра на сториците да е по-голяма от 5!")
else:
    print(f"Броя на положителните числа, чиято цифра на стотиците е"
          f" по-голяма от 5 е: {count_positive_divided_by_five}")

count_one_digit_nums = 0
sum_of_one_digit_nums = 0
for number in arr:
    if -9 <= number <= 9:
        count_one_digit_nums += 1
        sum_of_one_digit_nums += number
if count_one_digit_nums == 0:
    print("Няма едноцифрени числа в листа!")
else:
    average = sum_of_one_digit_nums/count_one_digit_nums
    print(f"Средно аритметичното на едноцифрените числа е: {average}.")

arr2 = []
for number in arr:
    if number % 9 == 0:
        arr2.append(number)
        print(f"Добавихте числото {number} към втория списък!")

num_even_elements_odd_index = 0
for idx in range(len(arr2)):
    if idx % 2 != 0: #нечетен индекс
        if arr2[idx] % 2 == 0:  #четна стойност
            num_even_elements_odd_index += 1
if num_even_elements_odd_index == 0:
    print("Няма четни елементи на нечетен индекс в листа!")
else:
    print(f"Броя на четните елементи на нечетен индекс в листа са: {num_even_elements_odd_index}")

for idx in range(len(arr2)):
    if arr2[idx] < 0: #проверяваме всички числа на дадения индекс
        print(f"Заменихте числото {arr2[idx]} в листа с 0")
        arr2[idx] = 0

print(f"Дължината на първия списък е: {len(arr)}")
print(f"Дължината на втория списък е: {len(arr2)}")
if len(arr2) < len(arr):
    while len(arr2) != len(arr):
        arr2.append(1)
else:
    print("Дължините на двата листа са равни")







