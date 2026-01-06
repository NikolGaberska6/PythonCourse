import random

while True:
  try:
        k = int(input("Въвдете число в интервала (30 ≤ k ≤ 80): "))
        if 30 <= k <= 80:
            break
        else:
            print("Моля въведете число в посочения интервал!")
  except:
        print("Моля въвдете валидни данни!")

x = random.randint(-8000, -2000)
y = random.randint(3000, 9000)
nums = []
for i in range(k):
    number = random.randint(x, y)
    nums.append(number)
    print(f"Успешно добавихте числото {number} в листа с числа!")

count_polidroms = 0
for number in nums:
    str_num = str(abs(number))
    if str_num[::-1] == str_num:
        count_polidroms += 1
if count_polidroms != 0:
    print(f"Броят на полидромните числа в листа е: {count_polidroms}")
else:
    print("В листа няма числа, които да са полидроми")

sum_nums_del4 = 0
for number in nums:
    if number % 4 == 0 and number % 8 != 0:
        sum_nums_del4 += number
if sum_nums_del4 != 0:
    print(f"Сумата на всички числа, които са кратни на 4, но не на 8 е: {sum_nums_del4}")
else:
    print("Няма числа в листа, които да са кратни на 4, но не и на 8!")

filtered = []
for number in nums:
    if 1000 <= abs(number) <= 9999:
        filtered.append(number)
        print(f"Успешно добавихте числото {number} към filtered.")

for idx in range(len(filtered)):
    if filtered[idx] < 0:
        current_num = filtered[idx]
        filtered.insert(idx + 1, 999)
        print(f"Добавихте 999 след числото {current_num}")

if len(filtered) % 2 != 0:
    mid_element = len(filtered) //2
    filtered.pop(mid_element)
    print("Премахнахте средния елемент в листа!")
