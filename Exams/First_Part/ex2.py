
while True:
  n = int(input("Въведете число в интервала (30 ≤ n ≤ 120): "))
  if 30 <= n <= 120:
     break
  else:
     print("Моля въведете число в посочения интервал!")

arr = []
while len(arr) < n:
    number = int(input("Моля въведете число в интервала: (-1000 : 1000): "))
    if -1000 <= number <= 1000:
        arr.append(number)
    else:
        print("Моля въведете число в посочения интервал!")

sum_number_start_2 = 0
for number in arr:
    str_digit = str(number)
    first_digit = str_digit[0]
    if first_digit == "2" or first_digit == "-2":
        sum_number_start_2 += number
if sum_number_start_2 != 0:
    print(f"Сумата на всички числа, които започват с цифра 2 или -2 е {sum_number_start_2}")
else:
    print("В листа няма числа, които да започваст с цифра 2 или -2")

sum_elements_end_0 = 0
count_elements_end_0 = 0
for number in arr:
    last_digit = abs(number) % 10
    if last_digit == 0:
        count_elements_end_0 += 1
        sum_elements_end_0 += number
if count_elements_end_0 != 0:
   average = sum_elements_end_0/count_elements_end_0
   print(f"Средно-аритметично на всички елементи, завършващи на 0 е {average}")
else:
    print("Няма числа в листа, завършващи на 0")

list_D = []
diff_digits = 0
for number in arr:
    digits = set(str(abs(number))) #set - премахва всички еднакви цифри на числото ---> оставя само различните
    if len(digits) == 2: #ако дължината на digits = 2, значи има само 2 различни цифри
        list_D.append(number)
        print(f"Добавихте числото {number} към list_D.")

for idx in range(len(list_D)):
    if idx % 2 != 0:
        print(f"Заменихте числото {list_D[idx]} с 2024.")
        list_D[idx] = 2024

if len(arr) == len(list_D):
    new_list = arr + list_D
    print("Обединихте двата листа.")
if len(arr) > len(list_D):
    arr.pop(0)
    arr.pop(0)
    print("Премахнахте първите 2 елемента от arr.")
elif len(list_D) > len(arr):
    list_D.pop(0)
    list_D.pop(0)
    print("Премахнахте първите 2 елемента от list_D.")