import random
try:
    while True:
     n = int(input("Въведете число в интервала: (20 < m < 60): "))
     if 20 < n < 60:
        break
     else:
        print("Моля въведете число в посочения интервал!")
except:
    print("Моля въведете валидни данни!")

list1 = []
x = random.randint(-5000, -2000)
y = random.randint(2000, 7000)

while len(list1) < n:
    number = int(input(f"Въведете число в интервала {x} : {y} : "))
    if x < number < y:
        list1.append(number)
    else:
        print("Моля въведете число в посочения интервал: ")

count_positive_last_digit_even = 0
for number in list1:
    if number > 0:
        last_digit = number % 10
        if last_digit % 2 == 0:
            count_positive_last_digit_even += 1
if count_positive_last_digit_even != 0:
    print(f"Броя на положителните числа, с четна цифра "
          f"на единиците е: {count_positive_last_digit_even}")
else:
    print("Няма положителни числа, с четна цифра на единиците в листа!")

sum_3_digits_odd_numbers = 1
for number in list1:
    if 100 <= abs(number) <= 999 and abs(number) % 2 != 0:
        sum_3_digits_odd_numbers *= number
if sum_3_digits_odd_numbers != 1:
    print(f"Произведението на всички елементи, които са тризначни"
          f"и нечетни е: {sum_3_digits_odd_numbers}")
else:
    print("Няма елементи, които са тризначни и нечетни в листа!")

list2 = []
for number in list1:
    if number % 2 == 0:
        last_digit = abs(number) % 10
        if last_digit == 6:
            list2.append(number)
            print(f"Добавихте {number} към втория лист.")

for idx in range(len(list2)):
    if idx % 3 == 0:
        print(f"Заменихте числото {list2[idx]} с 0.")
        list2[idx] = 0

if len(list1) > len(list2):
    for number in list2.copy():
        last_digit = abs(number) % 10
        list2.append(last_digit)
        print(f"Добавихте {last_digit} към листа!")
    if len(list1) % 2 != 0:
        mid_element = len(list1) // 2
        list1.pop(mid_element)
        print("Премахнахте средния елемент от листа!")
    else:
        mid_element1 = len(list1) // 2 #десния
        mid_element2 = len(list1) // 2 - 1 #левия
        list1.pop(mid_element1) #махаме първо десния
        list1.pop(mid_element2)
        print("Премахнахте двата средни елемента от листа!")
elif len(list2) > len(list1):
    for number in list1.copy():
        last_digit = abs(number) % 10
        list1.append(last_digit)
        print(f"Добавихте {last_digit} към листа!")
    if len(list2) % 2 != 0:
        mid_element = len(list2) // 2
        list2.pop(mid_element)
        print("Премахнахте средния елемент от листа!")
    else:
        mid_element1 = len(list2) // 2 #десния
        mid_element2 = len(list2) // 2 - 1 #левия
        list2.pop(mid_element1) #махаме първо десния
        list2.pop(mid_element2)
        print("Премахнахте двата средни елемента от листа!")
else:
    print("Двата листа имат еднаква дължина!")
