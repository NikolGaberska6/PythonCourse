import sys
first_list = []
for i in range(20):
    number = int(input("Въведете число, което искате да добавите в листа: "))
    first_list.append(number)

min_number = sys.maxsize
#min_number = min(first_list)
max_number = -sys.maxsize
#max_number = max(first_list)

for number in first_list:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
sum_of_min_max = min_number + max_number
if sum_of_min_max != 0:
    print(f"Сумата от максималното и минималното число в листа е: {sum_of_min_max}")

count_odd_elements = 0
for number in first_list:
    if number % 2 != 0:
        count_odd_elements += 1
if count_odd_elements != 0:
    print(f"Броя на елементите с нечетна стойност е: {count_odd_elements}")
else:
    print("Няма елементи с нечетна стойност в листа!")

second_list = []
for number in first_list:
    if number % 5 == 0:
        second_list.append(number)
        print(f"Добавихте числото {number} във втория лист.")

second_max = -sys.maxsize
#second_max = max(second_list)

sum_elements = 0
count_elements = 0
diff = 0
for number in second_list:
    if number > second_max:
        second_max = number
    sum_elements += number
    count_elements += 1
if count_elements != 0:
    average = sum_elements/count_elements
    diff = abs(second_max - average)
    print(f"Разликата на максималната стойност и средноаритметичното е: {diff}")

if len(second_list) > 0:
   first_element_second_list = second_list[0]
   last_element_second_list = second_list[-1]
   sum_of_elements = first_element_second_list + last_element_second_list
   second_list.append(sum_of_elements)
   print(f"Добавихте нов елемент към втория лист: {sum_of_elements}")
else:
    print("Листът е празен!")