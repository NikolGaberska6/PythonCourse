import random

values = []
for i in range(50):
    number = random.randint(10, 500)
    values.append(number)
    print(f"Успешно добавихте числото {number} в листа!")

multiply_sum = values[1] * values[3] * values[7]
print(f"Произведението на елементите на 1, 3 и 7ми индекс е: {multiply_sum}.")

count_odd_elements = 0
for number in values:
    if number % 2 != 0:
        count_odd_elements += 1
if count_odd_elements != 0:
    print(f"Броя на нечетните числа в листа е: {count_odd_elements}.")
else:
    print("Няма нечетни числа в листа!")

div_by_5 = []
for number in values:
    if number % 5 == 0:
        div_by_5.append(number)
        print(f"Успешно добавихте числото {number} във втория лист!")

if len(div_by_5) > 0:
    sum_of_el = 0
    average = 0
    for number in div_by_5:
        sum_of_el += number
    average = sum_of_el / len(div_by_5)
    print(f"Средноаритметичната стойност на числата в списъка е: {average:.2f}.")

    div_by_5.pop(2) #първо по-големия и после по-малкия елемент
    div_by_5.pop(0)
    print("Изтрихте елементите на индекси 0 и 2 от листа!")

else:
    print("Няма числа от първия списък кратни на 5.")
    print("Втория списък е празен!")

