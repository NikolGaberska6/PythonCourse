import random
while True:
  n = int(input("Въведете число в интервала (50 ≤ n ≤ 150): "))
  if 50 <= n <= 150:
      break
  else:
      print("Моля въведете число в посочения интервал!")

list_M = []
for i in range(n):
    number = random.randint(-777, 777)
    list_M.append(number)
    print(f"Добавихте {number} в листа.")

sum_of_numbers_del11 = 0
for number in list_M:
    if number % 11 == 0:
        sum_of_numbers_del11 += number
if sum_of_numbers_del11 != 0:
    print(f"Сумата на числата, които са кратни на 11 е {sum_of_numbers_del11}")
else:
    print("Няма числа, които да са кратни на 11 в листа.")

count_numbers_des10 = 0
for number in list_M:
    des_num = (number // 10) % 10
    if des_num == 0:
        count_numbers_des10 += 1
if count_numbers_des10 != 0:
    print(f"Броя на числата, чиято цифра на десетиците е 0 е {count_numbers_des10}")
else:
    print("Няма числа, чията цифра на десетиците да е 0 в листа.")

list_R = []
for number in list_M:
    if 100 <= number <= 999:
        last_digit = abs(number) % 10
        if last_digit == 8:
            list_R.append(number)
            print(f"Добавихте числото {number} към втория лист.")

for idx in range(len(list_R)):
    if idx % 5 == 0:
        print(f"Заменихте числото {list_R[idx]} с 1000.")
        list_R[idx] = 1000

if len(list_M) > len(list_R):
    list_M = list_M[3:]
    print("Премахнвахте първите 3 елемента от листа.")
elif len(list_R) > len(list_M):
    list_R = list_R[:-3]
    print("Премахнахте последните 3 елемента от листа.")