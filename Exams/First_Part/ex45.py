import random

while True:
    try:
       n = int(input("Въведете число в интервала (35 < n < 90): "))
       if 35 < n < 90:
          break
       else:
          print("Моля въведете число в посочения интервал!")
    except ValueError:
          print("Моля въведете валидни данни!")

a = random.randint(-9000, -3000)
b = random.randint(4000, 10000)
nums = []
for i in range(n):
    number = random.randint(a, b)
    nums.append(number)
    print(f"Успешно добавихте числото {number} в списъка с числа!")

count_negative_nums_same_digits = 0
for number in nums:
    if number < 0:
        str_number = str(abs(number))
        for digit in str_number:
            digit_found = False
            if str_number.count(digit) > 1:
                digit_found = True
                count_negative_nums_same_digits += 1
                break
if count_negative_nums_same_digits != 0:
    print(f"Броя на отрицателните числа, с повтарящи се цифри е: {count_negative_nums_same_digits}.")
else:
    print("Няма отрицателни числа с повтарящи се цифри!")

sum_of_positive_del_12 = 0
for number in nums:
    if number > 0:
        if number % 12 == 0:
            sum_of_positive_del_12 += number
if sum_of_positive_del_12 != 0:
    print(f"Намерете сумата на всички числа, които са кратни на 12 и са положителни е: {sum_of_positive_del_12}.")
else:
    print("Няма числа, които са кратни на 12 и са положителни!")

nums_2 = []
for number in nums:
    count_digits = 0
    str_number = str(abs(number))
    for digit in str_number:
        count_digits += 1
    if count_digits == 5:
        nums_2.append(number)
        print(f"ДОбавихте числото {number} към втория списък!")

if len(nums_2) == 0:
    print("Вторият списък е празен!")
else:
    for idx in range(len(nums_2)):
      current_element = nums_2[idx]
      last_digit = current_element % 10
      if last_digit == 7:
        print(f"Заменихте числото {current_element} с 777.")
        nums_2[idx] = 777