while True:
    m = int(input("Въведете число в интервала (30 ≤ m ≤ 75): "))
    if 30 <= m <= 75:
        break
    else:
        print("Моля въведете число в посочения интервал!")

arr = []
while len(arr) < m:
    number = int(input("Въведете число в интервала [-6000, 6000]: "))
    if -6000 <= number <= 6000:
        arr.append(number)
        print("Успешно добавихте числото в листа!")
    else:
        print("Моля въведете число в посочения интервал!")

count_hundreds_digit4 = 0
for number in arr:
    digit_of_hundreds = (abs(number) // 100) % 10
    if digit_of_hundreds == 4:
        count_hundreds_digit4 += 1
if count_hundreds_digit4 != 0:
    print(f"Броя на числата, които имат цифра на стотиците равна на 4 е: '{count_hundreds_digit4}'.")
else:
    print("В листа няма числа, които имат цифра на стотиците равна на 4!")

negative_even_nums = []
for number in arr:
    if number < 0 and number % 2 == 0:
        negative_even_nums.append(number)
if len(negative_even_nums) > 0:
    max_negative_num = max(negative_even_nums)
    print(f"Най голямото отрицателно четно число е: '{max_negative_num}'.")
else:
    print("В листа няма отрицателни четни числа!")

arr_2 = []
for number in arr:
    str_number = str(abs(number))
    reversed_num = str_number[::-1]
    if str_number == reversed_num:
        arr_2.append(number)
        print(f"Добавихте числото '{number}' към втория списък.")

for idx in range(len(arr_2)):
    if idx % 2 == 0:
        print(f"Заменихте числото {arr_2[idx]} с -999.")
        arr_2[idx] = -999

if len(arr) == len(arr_2):
    arr.reverse()
    print("Обърнахте списъка arr.")