while True:
  t = int(input("Въведете число в интервала (25 < t < 80): "))
  if 25 < t < 80:
     break
  else:
     print("Моля въведете число в посочения интервал!")

list_А = []
while len(list_А) < t:
    number = int(input("Моля въведете число в интервала: -20000 : 20000: "))
    if -20000 <= number <= 20000:
     list_А.append(number)
     print(f"Добавихте числото {number} с листа!")
    else:
        print("Моля въведете число в посочения интервал!")

multiplication_2digits_negative_nums = 1
for number in list_А:
    if -99 <= number <= -10:
        multiplication_2digits_negative_nums *= number
if multiplication_2digits_negative_nums != 1:
    print(f"Произведението на всички отрицателни двуцифрени числа"
          f" е: {multiplication_2digits_negative_nums}")
else:
    print("В листа няма отрицателни, двуцифрени числа!")

count_digit_element1 = 0
for number in list_А:
    digit_of_decimal = (abs(number) // 10) % 10
    if digit_of_decimal == 1:
        count_digit_element1 += 1
if count_digit_element1 != 0:
    print(f"Броя на елементи, чието число на десетиците "
          f"е 1 е {count_digit_element1}.")
else:
    print("Няма елементи в листа, чието число на десецитиците да е 1!")

list_B = []
for number in list_А:
    if 100 <= abs(number) <= 999:
        sum_of_digits = 0
        current_num = abs(number) #взимаме сегашното число
        while current_num > 0:
            last_digit = current_num % 10 #взимаме последната цифра на числото
            sum_of_digits += last_digit #добавяме към сумата от цифрите
            current_num = current_num // 10 #махаме последната цифра
        if sum_of_digits > 10:
            list_B.append(number)
            print(f"Добавихте {number} към втория лист.")

for idx in range(len(list_B)):
    if idx % 2 == 0:
        print(f"Заменихте числото {list_B[idx]} с 100.")
        list_B[idx] = 100

if len(list_А) > len(list_B):
    mid_element = len(list_А) // 2 #индекса на средния елемент
    list_А.pop(mid_element)
    print("Премахнахте средния елемент на list_A.")
elif len(list_B) > len(list_А):
    first_element = list_B[0]
    list_B.append(first_element)
    print(f"Добахте първия елемент ({first_element}) на list_B в края му.")
else:
    print("Двата листа имат еднакви дължини.")